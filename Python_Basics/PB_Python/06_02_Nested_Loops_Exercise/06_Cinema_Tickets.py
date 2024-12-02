total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

movie_name = input()

while movie_name != 'Finish':
    free_seats = int(input())
    sold_tickets = 0

    ticket_type = input()
    while ticket_type != 'End':
        sold_tickets += 1
        total_tickets += 1

        if ticket_type == 'student':
            student_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
        elif ticket_type == 'kid':
            kid_tickets += 1

        if sold_tickets >= free_seats:
            break

        ticket_type = input()

    percentage_full = (sold_tickets / free_seats) * 100
    print(f'{movie_name} - {percentage_full:.2f}% full.')

    movie_name = input()

student_percentage = (student_tickets / total_tickets) * 100
standard_percentage = (standard_tickets / total_tickets) * 100
kid_percentage = (kid_tickets / total_tickets) * 100

print(f'Total tickets: {total_tickets}')
print(f'{student_percentage:.2f}% student tickets.')
print(f'{standard_percentage:.2f}% standard tickets.')
print(f'{kid_percentage:.2f}% kids tickets.')
