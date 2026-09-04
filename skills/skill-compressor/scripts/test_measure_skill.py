import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('measure', Path(__file__).with_name('measure_skill.py'))
measure = importlib.util.module_from_spec(spec)
spec.loader.exec_module(measure)


class MeasurementTests(unittest.TestCase):
    def test_transitive_links_cycles_and_binary_assets(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            (root / 'references').mkdir()
            (root / 'SKILL.md').write_text('[step](procedure.md)')
            (root / 'procedure.md').write_text('[nested](references/nested.md#heading)')
            (root / 'references/nested.md').write_text('[cycle](../procedure.md)')
            (root / 'references/image.png').write_bytes(b'\xff\x00')
            found = measure.discover_reference_files(root, (root / 'SKILL.md').read_text())
            self.assertEqual({str(p.relative_to(root)) for p in found}, {'procedure.md', 'references/nested.md'})

    def test_invalid_probabilities(self):
        for probability in [-2, 2, float('nan'), float('inf'), True, '0.5']:
            with self.subTest(probability=probability), self.assertRaises(ValueError):
                measure.route_cost({'routes': [{'frequency': probability, 'files': []}]}, {}, set())

    def test_complete_distribution_required(self):
        for routes in [[], [{'frequency': 0.5}], [{'frequency': 0.7}, {'frequency': 0.7}]]:
            with self.subTest(routes=routes), self.assertRaises(ValueError):
                measure.route_cost({'routes': routes}, {}, set())

    def test_required_files_and_duplicate_loads(self):
        cost, rows = measure.route_cost({'routes': [
            {'frequency': 0.25, 'files': ['a.md', 'a.md', 'b.md']},
            {'frequency': 0.75, 'files': []},
        ]}, {'a.md': {'tokens': 10}, 'b.md': {'tokens': 20}}, {'a.md'})
        self.assertEqual(cost, 15)
        self.assertEqual(rows[0]['tokens'], 30)

    def test_unknown_files(self):
        with self.assertRaises(ValueError):
            measure.route_cost({'routes': [{'frequency': 1, 'files': ['missing.md']}]}, {}, set())

    def test_unknown_expected_cost_and_explicit_required_load(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'SKILL.md').write_text('---\nname: test\ndescription: test\n---\nRead [rule](rule.md).')
            (root / 'rule.md').write_text('A required instruction. ' * 20)
            command = [sys.executable, str(Path(__file__).with_name('measure_skill.py')), str(root)]
            unknown = json.loads(subprocess.check_output(command, text=True))
            required = json.loads(subprocess.check_output(command + ['--required', 'rule.md'], text=True))
            self.assertIsNone(unknown['expected_loaded_tokens'])
            self.assertEqual(required['minimum_loaded_tokens'], required['full_surface_tokens'])
            self.assertGreater(required['minimum_loaded_tokens'], unknown['minimum_loaded_tokens'])


if __name__ == '__main__':
    unittest.main()
