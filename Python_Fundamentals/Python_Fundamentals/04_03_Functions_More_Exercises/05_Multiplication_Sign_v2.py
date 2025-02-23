num_1 = float(input())
num_2 = float(input())
num_3 = float(input())

if 0 in (num_1, num_2, num_3):
    print('zero')
elif ((num_1 < 0) + (num_2 < 0) + (num_3 < 0)) % 2 == 0:  # use boolean arithmetic
    print('positive')
else:
    print('negative')
