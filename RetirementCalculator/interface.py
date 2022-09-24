from concurrent.futures import process
from fileinput import close
from .retirement_calculator import processor


class RetirementInterface:
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
        self.user_pre_retirement_monthly_income = float(input("\nStage 1:\n\nEnter your pre-retirement final monthly income: $"))
        self.user_annual_rate_of_return = float(input("Enter your expect rate of return (usually .03-.07): "))
        self.user_years_to_retire = float(input("Enter the number of years you hope to be retired (usually 15 - 30): "))

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
        self.user_years_until_retirement = float(input("\nStage 2\n\nHow many years until you retire?: "))
        self.user_average_monthly_investment = float(input("What will your average monthly investment be?: "))
        self.user_expected_retirement_return = float(input("Enter your expected annual retirement account return (usually .03 - .12): " ))

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
        self.user_request_details = str(input("\nStage 3\n\nDo you want to see your retirement summary? (y/n): "))
        self.user_retirement_surplus_or_deficit = self.user_account_balance - self.lump_sum_amount

        if self.user_request_details in ['y', 'Y', 'yes', 'Yes', "YES"]:
            if self.is_user_retirement_goal_met:
                return "\nFor {0} years in retirement, you want {1} in monthly income with {2} coming from investments.\
                    \nYou saved {3} monthly for {4} years.\
                    \nThis results in a retirement account balance surplus of {5}.".format(
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
                \nThis results in a retirement account balance deficit of {5}.".format(
                    round(self.user_years_to_retire),
                    "${:,.2f}".format(self.user_pre_retirement_monthly_income),
                    "${:,.2f}".format(self.user_monthly_withdrawal),
                    "${:,.2f}".format(self.user_average_monthly_investment),
                    round(self.user_years_until_retirement),
                    "-${:,.2f}".format(self.user_retirement_surplus_or_deficit * -1)
                )
        elif self.user_request_details in ['n', 'N', 'no', 'No', "NO"]:
            exit("Thank you for using Jared's Retirement Calculator, and see you again soon!")
        else:
            raise Exception("Please enter characters only, and try again.")

if __name__ == '__RetirementInterface__':
    RetirementInterface()