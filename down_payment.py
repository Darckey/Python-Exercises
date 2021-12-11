house_price = 1000000
buyer_credit = int(input("what is your credit? "))
good_buyer_down_payment = house_price * 0.1
bad_buyer_down_payment = house_price * 0.2

if buyer_credit >= 500000:
    print(f'You have a good credit and your down payment is {good_buyer_down_payment}!')
else:
    print(f'You have a bad credit and your down payment is {bad_buyer_down_payment}!')