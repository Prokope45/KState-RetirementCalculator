# import retirement_calculator.processor

class RetirementInterface:
    def __init__(self, pre_retirement_income=0.0, retirement_years=0.0, annual_rate_of_return=0.0):
        self.pre_retirement_income = pre_retirement_income
        self.retirement_years = retirement_years
        self.annual_rate_of_return = annual_rate_of_return
    
    def process_request(self):
        # TODO: Process request here instead of main.py
        pass

    def __str__(self):
        return f"{self.pre_retirement_income}"
