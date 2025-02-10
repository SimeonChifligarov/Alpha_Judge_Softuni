# Write a program that receives a single string (cards separated by space) and
# on the second line receives a number of faro shuffles that have to be made.
# Print the state of the deck after the shuffle.

string_of_card = input().split()
number_of_shuffles = int(input())
current_str_card = string_of_card
half_deck = int(len(string_of_card) / 2)
for shuffle in range(number_of_shuffles):
    left_side = current_str_card[:half_deck]
    right_side = current_str_card[half_deck:]
    current_str_card = []
    for index in range(len(left_side)):
        current_str_card.append(left_side[index])
        current_str_card.append(right_side[index])

print(current_str_card)
