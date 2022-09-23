from .retirement_calculator import processor

class RetirementInterface:
    def __init__(self):
        pass

    def monthly_interest_rate(self):
        print(processor.RetirementCalculator(annual_interest_rate=0.10).monthly_interest_rate())
    
    def stage_one(self):
        user_process = str(input("Welcome to the Retirement Calculator! Enter \"q\" to quit."))
        while user_process not in  ['n', 'q']:
            user_pre_retirement_monthly_income = int(input("Enter your pre-retirement final monthly income: "))
            user_years_to_retire = int(input("Enter the number of years you hope to retire: "))
            user_annual_rate_of_return = float(input("Enter your expect rate of return (usually .03-.07): " ))


            user_process = str(input("Do you want to continue? y/n or q"))
    
    def stage_two(self):
        pass

    def stage_three(self):
        pass

    def __str__(self):
        return f"{self.pre_retirement_income}"
