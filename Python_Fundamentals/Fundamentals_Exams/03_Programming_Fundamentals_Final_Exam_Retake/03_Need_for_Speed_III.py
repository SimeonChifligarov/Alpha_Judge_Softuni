n = int(input())

cars = {}
for _ in range(n):
    name, mileage, fuel = input().split("|")
    cars[name] = [int(mileage), int(fuel)]

while True:
    line = input()
    if line == "Stop":
        break
    parts = [p.strip() for p in line.split(" : ")]
    cmd = parts[0]
    if cmd == "Drive":
        car, distance, fuel = parts[1], int(parts[2]), int(parts[3])
        if cars[car][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car][0] += distance
            cars[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car][0] >= 100000:
                del cars[car]
                print(f"Time to sell the {car}!")
    elif cmd == "Refuel":
        car, fuel = parts[1], int(parts[2])
        space = 75 - cars[car][1]
        added = fuel if fuel <= space else space
        cars[car][1] += added
        print(f"{car} refueled with {added} liters")
    elif cmd == "Revert":
        car, km = parts[1], int(parts[2])
        new_mileage = cars[car][0] - km
        if new_mileage < 10000:
            cars[car][0] = 10000
        else:
            cars[car][0] = new_mileage
            print(f"{car} mileage decreased by {km} kilometers")

for car, (mileage, fuel) in cars.items():
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")
