import re
import unittest
from pathlib import Path


class TestCollisionAvoidanceDocs(unittest.TestCase):
    def test_step_3_points_to_collision_avoidance_folder(self):
        """Step 3 of collision_avoidance.md must navigate to the collision_avoidance folder."""
        doc_path = (
            Path(__file__).resolve().parent.parent
            / "docs"
            / "examples"
            / "collision_avoidance.md"
        )
        self.assertTrue(doc_path.exists(), f"Documentation file not found: {doc_path}")
        content = doc_path.read_text()
        match = re.search(
            r"^#### Step 3 - Optimize the model on Jetson Nano.*?(?=^#### |\\Z)",
            content,
            re.MULTILINE | re.DOTALL,
        )
        self.assertIsNotNone(match, "Step 3 section not found")
        navigate_lines = [line for line in match.group(0).splitlines() if "Navigate to" in line]
        self.assertTrue(navigate_lines, "No 'Navigate to' line in Step 3")
        for line in navigate_lines:
            self.assertIn("collision_avoidance", line, f"Step 3 navigates to wrong folder: {line}")


