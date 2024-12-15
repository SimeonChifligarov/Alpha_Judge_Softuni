def wedding_seating(last_sector, first_sector_rows, odd_row_seats):
    result = []
    for sector in range(ord('A'), ord(last_sector) + 1):
        sector_char = chr(sector)
        sector_rows = first_sector_rows + (sector - ord('A'))
        for row in range(1, sector_rows + 1):
            seats_in_row = odd_row_seats if row % 2 != 0 else odd_row_seats + 2
            for seat in range(1, seats_in_row + 1):
                seat_char = chr(ord('a') + seat - 1)
                result.append(f'{sector_char}{row}{seat_char}')

    return result


l_sector = input()
f_sector_rows = int(input())
odd_r_seats = int(input())

res = wedding_seating(last_sector=l_sector, first_sector_rows=f_sector_rows, odd_row_seats=odd_r_seats)

print('\n'.join(res))
print(len(res))
