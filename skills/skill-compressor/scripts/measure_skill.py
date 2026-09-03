#!/usr/bin/env python3
"""Measure catalog, always-loaded, routed, and full skill token surfaces."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def tokenizer():
    try:
        import tiktoken  # type: ignore
        enc = tiktoken.get_encoding("o200k_base")
        return lambda text: len(enc.encode(text)), "tiktoken:o200k_base"
    except Exception:
        return lambda text: (len(text) + 3) // 4, "estimate:ceil(chars/4)"


def split_frontmatter(text: str) -> tuple[str, str]:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n?", text, re.S)
    return (match.group(1), text[match.end():]) if match else ("", text)


def discover_reference_files(root: Path, main_text: str) -> list[Path]:
    """Find conventional references plus existing local Markdown paths named by SKILL.md."""
    found: set[Path] = set()
    references = root / "references"
    if references.exists():
        found.update(path.resolve() for path in references.glob("**/*") if path.is_file())
    candidates = re.findall(r"\[[^\]]*\]\(([^)#?]+\.md)\)|`([^`\n]+\.md)`", main_text)
    for groups in candidates:
        relative = next((value for value in groups if value), "").strip()
        if not relative or "://" in relative or Path(relative).is_absolute():
            continue
        path = (root / relative).resolve()
        try:
            path.relative_to(root)
        except ValueError:
            continue
        if path.is_file() and path != (root / "SKILL.md").resolve():
            found.add(path)
    return sorted(found)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill", type=Path)
    parser.add_argument("--routes", type=Path, help="JSON: {routes:[{files:[...],frequency:0..1}]} ")
    args = parser.parse_args()
    root = args.skill.resolve()
    main_file = root / "SKILL.md"
    if not main_file.is_file():
        raise SystemExit(f"missing {main_file}")
    count, method = tokenizer()
    main_text = main_file.read_text(encoding="utf-8")
    frontmatter, body = split_frontmatter(main_text)
    refs = discover_reference_files(root, main_text)
    files = {str(path.relative_to(root)): path.read_text(encoding="utf-8") for path in refs}
    metrics = {name: {"tokens": count(text), "words": len(text.split()), "bytes": len(text.encode())} for name, text in files.items()}
    catalog_tokens = count(frontmatter)
    body_tokens = count(body)
    expected_routed = 0.0
    route_rows = []
    if args.routes:
        data = json.loads(args.routes.read_text(encoding="utf-8"))
        for route in data.get("routes", []):
            frequency = float(route["frequency"])
            route_tokens = sum(metrics[name]["tokens"] for name in route.get("files", []))
            expected_routed += frequency * route_tokens
            route_rows.append({"files": route.get("files", []), "frequency": frequency, "tokens": route_tokens})
    result = {
        "skill": str(root),
        "token_method": method,
        "catalog_tokens": catalog_tokens,
        "always_loaded_tokens": catalog_tokens + body_tokens,
        "body_tokens": body_tokens,
        "reference_tokens": sum(row["tokens"] for row in metrics.values()),
        "full_surface_tokens": catalog_tokens + body_tokens + sum(row["tokens"] for row in metrics.values()),
        "expected_loaded_tokens": round(catalog_tokens + body_tokens + expected_routed, 2),
        "routes": route_rows,
        "files": metrics,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
