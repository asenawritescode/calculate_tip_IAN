import unittest

from main import calculate_tip

class TestCalculateTip(unittest.TestCase):
    def setUp(self):
        self.TIP_RANGE_BELOW = 0.15
        self.TIP_RANGE_ABOVE = 0.20

    def test_calculate_tip_within_range_below(self):
        amount = 100.0
        expected_tip = amount * self.TIP_RANGE_BELOW
        expected_total = amount + expected_tip
        result = calculate_tip(amount)
        self.assertEqual(result, f"Your bill is {amount}, your tip is {expected_tip}, and your total value is {expected_total}")

    def test_calculate_tip_within_range_above(self):
        amount = 350.0
        expected_tip = amount * self.TIP_RANGE_ABOVE
        expected_total = amount + expected_tip
        result = calculate_tip(amount)
        self.assertEqual(result, f"Your bill is {amount}, your tip is {expected_tip}, and your total value is {expected_total}")

    def test_calculate_tip_outside_ranges(self):
        amount = 50.0
        expected_tip = 0
        expected_total = amount + expected_tip
        result = calculate_tip(amount)
        self.assertEqual(result, f"Your bill is {amount}, your tip is {expected_tip}, and your total value is {expected_total}")

    def test_calculate_tip_invalid_amount(self):
        amount = "invalid"
        with self.assertRaises(ValueError):
            calculate_tip(amount)

if __name__ == "__main__":
    unittest.main()