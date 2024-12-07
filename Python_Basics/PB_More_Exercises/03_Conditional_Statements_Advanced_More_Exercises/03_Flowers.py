chrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
is_holiday = input()

if season in ['Spring', 'Summer']:
    chrysanthemum_price = 2.00
    rose_price = 4.10
    tulip_price = 2.50
elif season in ['Autumn', 'Winter']:
    chrysanthemum_price = 3.75
    rose_price = 4.50
    tulip_price = 4.15
else:
    chrysanthemum_price = None
    rose_price = None
    tulip_price = None
    raise ValueError('non valid <season> input')

total_price = (
    chrysanthemums_count * chrysanthemum_price +
    roses_count * rose_price +
    tulips_count * tulip_price
)

if is_holiday == 'Y':
    total_price *= 1.15

if season == 'Spring' and tulips_count > 7:
    total_price *= 0.95

if season == 'Winter' and roses_count >= 10:
    total_price *= 0.90

if chrysanthemums_count + roses_count + tulips_count > 20:
    total_price *= 0.80

total_price += 2  # Price for arranging the bouquet

print(f'{total_price:.2f}')
