import math

price_per_racket = float(input())
number_of_rackets = int(input())
number_of_shoes = int(input())

price_per_shoe = price_per_racket / 6
total_racket_price = price_per_racket * number_of_rackets
total_shoe_price = price_per_shoe * number_of_shoes
equipment_price = (total_racket_price + total_shoe_price) / 5  # * 0.2

total_price = total_racket_price + total_shoe_price + equipment_price

price_paid_by_djokovic = math.floor(total_price / 8)
price_paid_by_sponsors = math.ceil(total_price * 7 / 8)

print(f'Price to be paid by Djokovic {price_paid_by_djokovic}')
print(f'Price to be paid by sponsors {price_paid_by_sponsors}')
