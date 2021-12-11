# New loan is granted only if years income is over 50k/year and existing loans are less than 50% of years income. 

year_income = int(input("What is your year income? "))
credit = int(input("How much you have loans? "))
credit_ratio = credit/year_income

good_income = None  
good_credit = None

if year_income >= 50000:
    good_income = True
else:
    bad_income = True

if credit_ratio < 0.5:
    good_credit = True
else:
    bad_credit = True 

if good_income and good_credit:
    print("Your loan is granted!")
else:
    print("Conditions not met!")