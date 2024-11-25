n = int(input())
salary = float(input())

penalties = {
    'Facebook': 150,
    'Instagram': 100,
    'Reddit': 50,
}

for _ in range(n):
    website = input()

    if website in penalties:
        salary -= penalties[website]

    if salary <= 0:
        print('You have lost your salary.')
        break
else:
    print(int(salary))
