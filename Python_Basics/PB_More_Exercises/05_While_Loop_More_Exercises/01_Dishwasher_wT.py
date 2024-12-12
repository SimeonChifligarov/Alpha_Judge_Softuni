# using while True

bottles = int(input())
detergent = bottles * 750

dishes_washed = 0
pots_washed = 0
wash_count = 0

while True:
    line = input()

    if line == 'End':
        print('Detergent was enough!')
        print(f'{dishes_washed} dishes and {pots_washed} pots were washed.')
        print(f'Leftover detergent {detergent} ml.')
        break

    items_to_wash = int(line)
    wash_count += 1

    if wash_count % 3 == 0:
        detergent_needed = items_to_wash * 15
        pots_washed += items_to_wash
    else:
        detergent_needed = items_to_wash * 5
        dishes_washed += items_to_wash

    if detergent_needed > detergent:
        print(f'Not enough detergent, {detergent_needed - detergent} ml. more necessary!')
        break
        
    detergent -= detergent_needed
