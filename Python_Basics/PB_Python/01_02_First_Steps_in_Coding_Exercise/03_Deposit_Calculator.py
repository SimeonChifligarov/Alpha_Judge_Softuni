deposit_amount = float(input())
deposit_period = int(input())
annual_interest_rate = float(input())

annual_interest_rate_percent = annual_interest_rate / 100
interest = deposit_period * ((deposit_amount * annual_interest_rate_percent) / 12)

total_amount = deposit_amount + interest

print(total_amount)
