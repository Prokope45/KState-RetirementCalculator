

class RetirementCalculator:
    def __init__(
        self,
        monthly_withdraws: float=0.0,
        dollars_amount: float=0.0,
        monthly_interest: float=0.0,
        annual_interest_rate: float=0.0,
        retirement_years: float=0.0
    ):
        """ Initialized class members """
        self.monthly_withdraws = monthly_withdraws
        self.dollars_amount = dollars_amount
        self.retirement_years = retirement_years
        self.monthly_interest = monthly_interest
        self.annual_interest_rate = annual_interest_rate

        """ Lambda constants for evaluating lump sum, account balance, monthly withdrawal during retirement, and monthly interest rates """
        self.LUMP_SUM = lambda monthly_withdraws, retirement_years, annual_interest_rate: \
            monthly_withdraws * ((1 - (1 + (annual_interest_rate / 12))**-(retirement_years * 12)) / (annual_interest_rate / 12))

        self.ACCOUNT_BALANCE = lambda monthly_deposits, retirement_years, annual_interest_rate: \
            monthly_deposits * ((((1 + (annual_interest_rate / 12))**(retirement_years * 12)) - 1) / (annual_interest_rate / 12))

        self.MONTHLY_WITHDRAWAL_FOR_RETIREMENT = lambda dollars_amount: dollars_amount - (dollars_amount * 0.15)
        self.MONTHLY_INTEREST_RATE = lambda annual_interest_rate: annual_interest_rate / 12

    def lump_sum(self):
        """ Return to user their lump sum amount for when they retire """
        try:
            return self.LUMP_SUM(
                self.MONTHLY_WITHDRAWAL_FOR_RETIREMENT(self.dollars_amount),
                self.retirement_years,
                self.annual_interest_rate
            )
        except Exception as exc:
            print("{0} has occurred.".format(exc))
    
    def account_balance(self):
        """ Return to user their account balance """
        try:
            return self.ACCOUNT_BALANCE(self.dollars_amount, self.retirement_years, self.annual_interest_rate)
        except Exception as exc:
            print("{0} has occurred.".format(exc))
    
    def monthly_withdrawal_for_retirement(self):
        """ Return the require monthly withdrawal to achieve desired income level """
        try:
            return self.MONTHLY_WITHDRAWAL_FOR_RETIREMENT(self.dollars_amount)
        except Exception as exc:
            print("{0} has occurred.".format(exc))
    
    def monthly_interest_rate(self):
        """ Return to user the monthly interest rate """
        try:
            return self.MONTHLY_INTEREST_RATE(self.annual_interest_rate)
        except Exception as exc:
            print("{0} has occurred.".format(exc))   