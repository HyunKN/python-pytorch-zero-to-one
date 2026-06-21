import contextlib
import importlib.util
import io
import unittest
from pathlib import Path


CHECKER_PATH = (
    Path(__file__).parents[1]
    / "leetcode"
    / "day-01-running-sum"
    / "check.py"
)


def load_checker():
    spec = importlib.util.spec_from_file_location("day01_check", CHECKER_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CheckerTests(unittest.TestCase):
    def run_checker(self, solution):
        self.assertTrue(CHECKER_PATH.exists(), "check.py must exist")
        checker = load_checker()
        output = io.StringIO()

        with contextlib.redirect_stdout(output):
            passed = checker.run_tests(solution)

        return passed, output.getvalue()

    def test_correct_solution_reports_all_tests_passed(self):
        def correct_solution(nums):
            result = []
            total = 0
            for number in nums:
                total += number
                result.append(total)
            return result

        passed, output = self.run_checker(correct_solution)

        self.assertTrue(passed)
        self.assertIn("Test 1: PASS", output)
        self.assertIn("Input:", output)
        self.assertIn("Expected Output:", output)
        self.assertIn("Your Output:", output)
        self.assertIn("4/4 tests passed", output)

    def test_wrong_solution_reports_expected_and_actual_output(self):
        passed, output = self.run_checker(lambda nums: nums)

        self.assertFalse(passed)
        self.assertIn("Test 1: FAIL", output)
        self.assertIn("Expected Output: [1, 3, 6, 10]", output)
        self.assertIn("Your Output:     [1, 2, 3, 4]", output)

    def test_exception_is_reported_without_stopping_remaining_tests(self):
        def broken_solution(nums):
            raise ValueError("example failure")

        passed, output = self.run_checker(broken_solution)

        self.assertFalse(passed)
        self.assertEqual(output.count(": FAIL"), 4)
        self.assertIn("ValueError: example failure", output)
        self.assertIn("0/4 tests passed", output)


if __name__ == "__main__":
    unittest.main()
