from RetirementCalculator import interface

user_process = str(input("Welcome to the Retirement Calculator! Enter \"q\" to quit."))
while user_process not in  ['n', 'q']:
    print("Stage 1:")
    user_pre_retirement_monthly_income = int(input("Enter your pre-retirement final monthly income: "))

    interface = interface.RetirementInterface(pre_retirement_income=user_pre_retirement_monthly_income)
    print(interface)
    user_process = str(input("Do you want to continue? y/n"))
