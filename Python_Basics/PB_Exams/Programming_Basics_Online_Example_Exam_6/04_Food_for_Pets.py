days = int(input())
total_food = float(input())

dog_eat_real = 0
cat_eat_real = 0
dog_biz = 0
total_eat = 0

for day in range(1, days + 1):
    dog_eat = int(input())
    cat_eat = int(input())
    dog_eat_real += dog_eat
    cat_eat_real += cat_eat
    day_eat = dog_eat + cat_eat
    total_eat += day_eat
    if day % 3 == 0:
        dog_biz += 0.10 * day_eat

print(f'Total eaten biscuits: {round(dog_biz)}gr.')
print(f'{((total_eat / total_food) * 100):.2f}% of the food has been eaten.')
print(f'{((dog_eat_real / total_eat) * 100):.2f}% eaten from the dog.')
print(f'{((cat_eat_real / total_eat) * 100):.2f}% eaten from the cat.')
