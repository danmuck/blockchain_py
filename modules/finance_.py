import os, json, datetime, math
from decimal import *

def calculate_monthly_gains() -> Decimal:
    '''
        Returns a Decimal value rounded 2 places just like moneys.
    '''
    starting_cash = Decimal(input("Enter Starting Cash Amount \n: $ "))
    interest_rate = Decimal(input("APY \n: % "))
    interest_calc_time = int(input("Interest paid out: \n  0: Year\n  1: Month\n  2: Day \n: "))
    investment = starting_cash
    total_interest_gain = 0
    match interest_calc_time:
        case 0:
            interest_div = 1
            calc_time_str = "years"
        case 1:
            interest_div = 12
            calc_time_str = "months"
        case 2:
            interest_div = 365
            calc_time_str = "days"
        case _:
            interest_div = 12
            calc_time_str = "months"
    
    j = int(input(f"How many {calc_time_str} will you calculate gains over? \n: "))

    for i in range(j):
        interest_gain = investment * ((interest_rate / 100) / interest_div)
        total_interest_gain += interest_gain

        print(f"\n  Month {i} start: ${round(investment, 2)}")
        investment = investment + interest_gain
        print(f"\tInterest: ${round(interest_gain, 2)}")
    else:
        print(f"\nInitial Investment: ${round(starting_cash, 2)} \nTotal interest gained over {j} months: ${round(total_interest_gain, 2)} \n")
    
        return round(investment, 2)
