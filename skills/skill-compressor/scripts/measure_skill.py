#!/usr/bin/env python3
"""Measure catalog, always-loaded, routed, and full skill token surfaces."""

from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path


def tokenizer(encoding="o200k_base", require=False):
    try:
        import tiktoken  # type: ignore
        enc = tiktoken.get_encoding(encoding)
        return lambda text: len(enc.encode(text, disallowed_special=())), f"tiktoken:{encoding}"
    except ImportError:
        if require:
            raise SystemExit("tiktoken unavailable; install it or use estimates for screening only")
        return lambda text: (len(text) + 3) // 4, "estimate:ceil(chars/4)"


def split_frontmatter(text: str) -> tuple[str, str]:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n?", text, re.S)
    return (match.group(1), text[match.end():]) if match else ("", text)


def discover_reference_files(root: Path, main_text: str) -> list[Path]:
    """Find conventional references plus existing local Markdown paths named by SKILL.md."""
    root = root.resolve()
    found: set[Path] = set()
    references = root / "references"
    main = (root / "SKILL.md").resolve()
    pending = [main]
    if references.exists():
        pending.extend(references.rglob("*.md"))
    visited = set()
    while pending:
        source = pending.pop().resolve()
        if source in visited or not source.is_relative_to(root) or not source.is_file():
            continue
        visited.add(source)
        if source != main:
            found.add(source)
        text = main_text if source == main else source.read_text(encoding="utf-8")
        candidates = re.findall(r"\[[^\]]*\]\(([^)#?]+\.md)(?:[?#][^)]*)?\)|`([^`\n]+\.md)`", text)
        for groups in candidates:
            relative = next((value for value in groups if value), "").strip()
            if relative and "://" not in relative and not Path(relative).is_absolute():
                pending.append(source.parent / relative)
    return sorted(found)


def route_cost(data, metrics, required):
    """Routes are mutually exclusive complete load scenarios, with probabilities summing to 1."""
    rows = []
    for route in data.get("routes", []):
        frequency = route["frequency"]
        if isinstance(frequency, bool) or not isinstance(frequency, (int, float)) or not math.isfinite(frequency) or not 0 <= frequency <= 1:
            raise ValueError("route frequency must be finite and between 0 and 1")
        names = set(route.get("files", [])) | required
        unknown = names - metrics.keys()
        if unknown:
            raise ValueError(f"unknown reference files: {sorted(unknown)}")
        rows.append({"files": sorted(names), "frequency": frequency,
                     "tokens": sum(metrics[name]["tokens"] for name in names)})
    if not math.isclose(sum(row["frequency"] for row in rows), 1.0, abs_tol=1e-9):
        raise ValueError("complete route probabilities must sum to 1; include an empty-files route when applicable")
    return sum(row["frequency"] * row["tokens"] for row in rows), rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill", type=Path)
    parser.add_argument("--routes", type=Path, help="Complete mutually exclusive load scenarios; probabilities sum to 1")
    parser.add_argument("--required", action="append", default=[], help="Required reference path, repeatable; include required nested files")
    parser.add_argument("--encoding", default="o200k_base", help="Tokenizer encoding; validate against the target runtime")
    parser.add_argument("--require-tokenizer", action="store_true", help="Fail instead of estimating when tiktoken is unavailable")
    args = parser.parse_args()
    root = args.skill.resolve()
    main_file = root / "SKILL.md"
    if not main_file.is_file():
        raise SystemExit(f"missing {main_file}")
    count, method = tokenizer(args.encoding, args.require_tokenizer)
    main_text = main_file.read_text(encoding="utf-8")
    frontmatter, body = split_frontmatter(main_text)
    refs = discover_reference_files(root, main_text)
    files = {str(path.relative_to(root)): path.read_text(encoding="utf-8") for path in refs}
    metrics = {name: {"tokens": count(text), "words": len(text.split()), "bytes": len(text.encode())} for name, text in files.items()}
    catalog_tokens = count(frontmatter)
    body_tokens = count(body)
    required = set(args.required)
    if required - metrics.keys():
        parser.error(f"unknown required references: {sorted(required - metrics.keys())}")
    minimum = catalog_tokens + body_tokens + sum(metrics[name]["tokens"] for name in required)
    expected = None
    route_rows = []
    if args.routes:
        data = json.loads(args.routes.read_text(encoding="utf-8"))
        try:
            expected_routed, route_rows = route_cost(data, metrics, required)
        except (ValueError, KeyError, TypeError) as error:
            parser.error(str(error))
        expected = round(catalog_tokens + body_tokens + expected_routed, 2)
    result = {
        "skill": str(root),
        "token_method": method,
        "catalog_tokens": catalog_tokens,
        "always_loaded_tokens": catalog_tokens + body_tokens,
        "body_tokens": body_tokens,
        "reference_tokens": sum(row["tokens"] for row in metrics.values()),
        "full_surface_tokens": catalog_tokens + body_tokens + sum(row["tokens"] for row in metrics.values()),
        "expected_loaded_tokens": expected,
        "minimum_loaded_tokens": minimum,
        "required_files": sorted(required),
        "routes": route_rows,
        "files": metrics,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
