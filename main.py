"""
File Name: main.py
Author: Jared Paubel
Description: Run unit tests before running main program
"""

# Module Imports
# none

# Relative Imports
from RetirementCalculator import interface
from RetirementCalculator.testRetirementCalculator import test_retirement_calculator

if __name__ == '__main__':
    print("Welcome to Jared's Retirement Calculator! \nLet's get started:")
    interface = interface.RetirementInterface()
    test_retire_calc = test_retirement_calculator.TestRetirementCalculator()

    # Ensure tests pass first
    test_retire_calc.test_monthly_interest_rate()
    test_retire_calc.test_monthly_withdrawal_for_retirement()
    test_retire_calc.test_lump_sum()
    test_retire_calc.test_account_balance()

    # run Stage One
    print(interface.stage_one())

    # run Stage Two
    print(interface.stage_two())

    # run Stage Three
    print(interface.stage_three())
