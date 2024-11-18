pens_price = 5.80
markers_price = 7.20
cleaner_price_per_liter = 1.20

pens_count = int(input())
markers_count = int(input())
cleaner_liters = int(input())
discount_percentage = int(input())

total_price = (
        pens_count * pens_price +
        markers_count * markers_price +
        cleaner_liters * cleaner_price_per_liter
)

discount = total_price * (discount_percentage / 100)
final_price = total_price - discount

print(final_price)
