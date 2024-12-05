n = int(input())  
period = input()  

taxi_base_price = 0.70  
if period == 'day':
    taxi_price = taxi_base_price + (n * 0.79)  
else:
    taxi_price = taxi_base_price + (n * 0.90)  

if n >= 20:
    bus_price = n * 0.09  
else:
    bus_price = float('inf')  

if n >= 100:
    train_price = n * 0.06  
else:
    train_price = float('inf')  

min_price = min(taxi_price, bus_price, train_price)

print(f'{min_price:.2f}')
