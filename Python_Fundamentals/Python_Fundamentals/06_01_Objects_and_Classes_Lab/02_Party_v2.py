class Party:
    def __init__(self):
        self.people = []


my_party = Party()

while True:
    name = input()

    if name == 'End':
        break

    my_party.people.append(name)

total_people_going = len(my_party.people)
print(f'Going: {", ".join(my_party.people)}')
print(f'Total: {total_people_going}')
