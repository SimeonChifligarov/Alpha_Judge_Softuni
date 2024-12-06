import math

days = int(input())
food_left = int(input())  
dog_food_per_day = float(input())  
cat_food_per_day = float(input())  
turtle_food_per_day_grams = float(input())  

turtle_food_per_day_kg = turtle_food_per_day_grams / 1000  

total_food_needed = (dog_food_per_day + cat_food_per_day + turtle_food_per_day_kg) * days  

if food_left >= total_food_needed:
    food_left_kg = food_left - total_food_needed
    print(f'{math.floor(food_left_kg)} kilos of food left.')
else:
    food_needed_more = total_food_needed - food_left
    print(f'{math.ceil(food_needed_more)} more kilos of food are needed.')
