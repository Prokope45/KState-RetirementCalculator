"""
File Name: interface.py
Author: Jared Paubel
Description: Serves as the medium between the user and the backend processing
"""

# Module Imports
# none

# Relative Imports
from .retirement_calculator import processor


class RetirementInterface:
    """Main interaction between user and backend processing for calculating retirement potentials

    Keyword Args:
        Stage One
        * user_pre_retirement_monthly_income: float = 0.0
        * user_annual_rate_of_return: float = 0.0
        * user_monthly_withdrawal: float = 0.0
        * user_years_to_retire: float = 0.0
        * lump_sum_amount: float = 0.0
        
        Stage Two
        * user_years_until_retirement: float = 0.0
        * user_average_monthly_investment: float = 0.0
        * user_expected_retirement_return: float = 0.0
        * user_account_balance: float = 0.0
        * is_user_retirement_goal_met: bool = False
        
        Stage Three
        * user_request_details: str
        * user_retirement_surplus_or_deficit: float = 0.0

    Methods:
        * monthly_interest_rate
        * stage_one
        * stage_two
        * stage_three

    """
    def __init__(self):
        # Stage One
        self.user_pre_retirement_monthly_income: float = 0.0
        self.user_annual_rate_of_return: float = 0.0
        self.user_monthly_withdrawal: float = 0.0
        self.user_years_to_retire: float = 0.0
        self.lump_sum_amount: float = 0.0

        # Stage Two
        self.user_years_until_retirement: float = 0.0
        self.user_average_monthly_investment: float = 0.0
        self.user_expected_retirement_return: float = 0.0
        self.user_account_balance: float = 0.0
        self.is_user_retirement_goal_met: bool = False

        # Stage Three
        self.user_request_details: str
        self.user_retirement_surplus_or_deficit: float = 0.0

    def monthly_interest_rate(self):
        return processor.RetirementCalculator(annual_interest_rate=0.10).monthly_interest_rate()

    def stage_one(self):
        """Get user input for pre-retirement monthly income, annual rate of return, and years to retire\n
        Return response with properly calculated values
        """
        try:
            self.user_input = input("\nStage 1:\n\nEnter your pre-retirement final monthly income: ")
            self.user_pre_retirement_monthly_income = float(self.user_input if self.user_input[0] != "$" else self.user_input[1:])

            self.user_input = input("Enter your expected rate of return (usually .03-.07): ")
            self.user_annual_rate_of_return = float(self.user_input) if self.user_input[-1] != "%" else float(self.user_input[:-1]) / 100

            self.user_years_to_retire = float(input("Enter the number of years you hope to be retired (usually 15 - 30): "))
        except ValueError:
            return "Please enter numerical values for all inputs."
        except IndexError:
            return "Please enter numerical values for all inputs."

        process_calculation = processor.RetirementCalculator(
            dollars_amount=self.user_pre_retirement_monthly_income, 
            annual_interest_rate=self.user_annual_rate_of_return, 
            retirement_years=self.user_years_to_retire
        )

        self.lump_sum_amount = process_calculation.lump_sum()
        self.user_monthly_withdrawal = process_calculation.monthly_withdrawal_for_retirement()

        return "\nYou will need to withdraw ${0:,.2f} every month from your investments to achieve a post-retirement income of ${1:,.2f}.\
            \nYou will need ${2:,.2f} in your investment accounts to achieve this income.".format(
            self.user_monthly_withdrawal, 
            self.user_pre_retirement_monthly_income,
            process_calculation.lump_sum()
        )

    def stage_two(self):
        """Get user input for average monthly investment, expected rate of return, and years until retirement\n
        Return response with properly calculated values
        """
        try:
            self.user_years_until_retirement = float(input("\nStage 2\n\nHow many years until you retire?: "))

            self.user_input = input("What will your average monthly investment be?: ")
            self.user_average_monthly_investment = float(self.user_input if self.user_input[0] != "$" else self.user_input[1:])

            self.user_input = input("Enter your expected annual retirement account return (usually .03 - .12): ")
            self.user_expected_retirement_return = float(self.user_input) if self.user_input[-1] != "%" else float(self.user_input[:-1]) / 100
        except ValueError:
            return "Please enter numerical values for all inputs."
        except IndexError:
            return "Please enter numerical values for all inputs."

        process_calculation = processor.RetirementCalculator(
            dollars_amount=self.user_average_monthly_investment, 
            annual_interest_rate=self.user_expected_retirement_return, 
            retirement_years=self.user_years_until_retirement
        )

        self.user_account_balance = process_calculation.account_balance()

        if self.user_account_balance >= self.lump_sum_amount:
            self.is_user_retirement_goal_met = True
            return "\nCongratulations! You will achieve your income goal.\n"
        else:
            self.is_user_retirement_goal_met = False
            return "\nUnfortunately, you will need to save more to reach your retirement goal.\n"

    def stage_three(self):
        """Get user input for whether they request to see the retirment account summary\n
        Return response with properly calculated values and close
        """
        try:
            self.user_request_details = str(input("\nStage 3\n\nDo you want to see your retirement summary? (y/n): "))
        except ValueError:
            return "Please enter character values for input."

        self.user_retirement_surplus_or_deficit = self.user_account_balance - self.lump_sum_amount

        if self.user_request_details in ['y', 'Y', 'yes', 'Yes', "YES"]:
            if self.is_user_retirement_goal_met:
                return "\nFor {0} years in retirement, you want {1} in monthly income with {2} coming from investments.\
                    \nYou saved {3} monthly for {4} years.\
                    \nThis results in a retirement account balance surplus of {5}.\
                    \n\nThank you for using Jared's Retirement Calculator, and see you again soon!".format(
                        round(self.user_years_to_retire),
                        "${:,.2f}".format(self.user_pre_retirement_monthly_income),
                        "${:,.2f}".format(self.user_monthly_withdrawal),
                        "${:,.2f}".format(self.user_average_monthly_investment),
                        round(self.user_years_until_retirement),
                        "${:,.2f}".format(self.user_retirement_surplus_or_deficit)
                    )
            else:
                return "\nFor {0} years in retirement, you want {1} in monthly income with {2} coming from investments.\
                \nYou saved {3} monthly for {4} years.\
                \nThis results in a retirement account balance deficit of {5}.\
                \n\nThank you for using Jared's Retirement Calculator, and see you again soon!".format(
                    round(self.user_years_to_retire),
                    "${:,.2f}".format(self.user_pre_retirement_monthly_income),
                    "${:,.2f}".format(self.user_monthly_withdrawal),
                    "${:,.2f}".format(self.user_average_monthly_investment),
                    round(self.user_years_until_retirement),
                    "-${:,.2f}".format(self.user_retirement_surplus_or_deficit * -1)
                )
        elif self.user_request_details in ['n', 'N', 'no', 'No', "NO"]:
            exit("\nThank you for using Jared's Retirement Calculator, and see you again soon!")
        else:
            raise Exception("Please enter characters only, and try again.")

if __name__ == '__RetirementInterface__':
    RetirementInterface()