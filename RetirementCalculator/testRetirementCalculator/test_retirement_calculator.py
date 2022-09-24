"""
File Name: test_retirement_calculator.py
Author: Jared Paubel
Section: 19C
Description: Unit testing to ensure processing functionaly works properly
"""

# Module Imports
import unittest

# Relative Imports
import RetirementCalculator.retirement_calculator.processor as processor


class TestRetirementCalculator(unittest.TestCase):
    """ Test the functionality of RetirementCalculator """

    def test_lump_sum(self):
        retire_calc = processor.RetirementCalculator(
            dollars_amount=8000.0,
            retirement_years=25.00,
            annual_interest_rate=0.05
        )

        output = float("{:.2f}".format(retire_calc.lump_sum()))
        expected = 1163208.32
        try:
            self.assertEqual(output, expected)
        except AssertionError as exc:
            raise AssertionError("Output is not the same as expected: \n{0}".format(exc))

    def test_account_balance(self):
        retire_calc = processor.RetirementCalculator(dollars_amount=900, annual_interest_rate=0.09, retirement_years=35)
        output = float("{:.2f}".format(retire_calc.account_balance()))
        try:
            self.assertGreaterEqual(output, 1163208.32)
        except AssertionError as exc:
            raise AssertionError("Output is not less than or equal to expected: \n{0}".format(exc))

    def test_monthly_withdrawal_for_retirement(self):
        retire_calc = processor.RetirementCalculator(dollars_amount=8000.00)
        output = float("{:.2f}".format(retire_calc.monthly_withdrawal_for_retirement()))
        expected = 6800.00
        try:
            self.assertEqual(output, expected)
        except AssertionError as exc:
            raise AssertionError("Output is not the same as expected: \n{0}".format(exc))

    def test_monthly_interest_rate(self):
        retire_calc = processor.RetirementCalculator(annual_interest_rate=0.05)
        output = float("{:.4f}".format(retire_calc.monthly_interest_rate()))
        expected = float("{:.4f}".format((0.05 / 12)))
        try:
            self.assertEqual(output, expected)
        except AssertionError as exc:
            raise AssertionError("Output is not the same as expected: \n{0}".format(exc))
