fruit_list = [
    'banana',
    'apple',
    'kiwi',
    'cherry',
    'lemon',
    'grapes',
]

vegetable_list = [
    'tomato',
    'cucumber',
    'pepper',
    'carrot',
]

product = input()

if product in fruit_list:
    print('fruit')
elif product in vegetable_list:
    print('vegetable')
else:
    print('unknown')
