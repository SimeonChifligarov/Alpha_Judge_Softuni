budget = float(input())
num_gpus = int(input())
num_processors = int(input())
num_ram = int(input())

gpu_price = 250
total_gpu_price = num_gpus * gpu_price

processor_price = 0.35 * total_gpu_price
ram_price = 0.10 * total_gpu_price

total_processor_price = num_processors * processor_price
total_ram_price = num_ram * ram_price

total_cost = total_gpu_price + total_processor_price + total_ram_price

if num_gpus > num_processors:
    total_cost *= 0.85  # 15% discount

if total_cost <= budget:
    remaining_budget = budget - total_cost
    print(f'You have {remaining_budget:.2f} leva left!')
else:
    required_money = total_cost - budget
    print(f'Not enough money! You need {required_money:.2f} leva more!')
