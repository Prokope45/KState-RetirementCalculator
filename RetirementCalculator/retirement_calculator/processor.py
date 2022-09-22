

class RetirementCalculator:
    def __init__(self, monthly_withdraws, dollars, monthly_interest, annual_interest_rate):
        """ Initialized class members """
        self.monthly_withdraws = monthly_withdraws
        self.dollars = dollars
        self.monthly_interest = monthly_interest
        self.annual_interest_rate = annual_interest_rate

        """ Lambda constants for evaluating lump sum, account balance and monthly interest rates """
        self.LUMP_SUM = lambda d, mw, mi: d * ((1 - 1(1 + mi)**-mw) / mi)
        self.ACCOUNT_BALANCE = lambda d, mw, mi: d * ((((1 + mi)**mw) - 1) / mi)
        self.MONTHLY_INTEREST_RATE = lambda annual_interest_rate: annual_interest_rate / 12
    
    def lump_sum(self):
        """ Return to user their lump sum amount for when they retire """
        try:
            return self.LUMP_SUM(self.dollars, self.monthly_withdraws, self.monthly_interest)
        except Exception as exc:
            print("{0} has occurred.".format(exc))
    
    def account_balance(self):
        """ Return to user their account balance """
        try:
            return self.ACCOUNT_BALANCE(self.dollars, self.monthly_withdraws, self.monthly_interest)
        except Exception as exc:
            print("{0} has occurred.".format(exc))        
    
    def monthly_interest_rate(self):
        """ Return to user the monthly interest rate """
        try:
            return self.MONTHLY_INTEREST_RATE(self.annual_interest_rate)
        except Exception as exc:
            print("{0} has occurred.".format(exc))   