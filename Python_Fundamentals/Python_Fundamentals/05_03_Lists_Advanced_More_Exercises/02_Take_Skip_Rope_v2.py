complete_message = list(input())

dig_from_complete_message = []
filtered_message = []

for el in complete_message:
    if el.isdigit():
        dig_from_complete_message.append(int(el))
    else:
        filtered_message.append(el)

complete_message = filtered_message

take_list = []
skip_list = []

for index, value in enumerate(dig_from_complete_message):
    if index % 2 == 0:
        take_list.append(value)
    else:
        skip_list.append(value)

final_message = []
message_index = 0

for take, skip in zip(take_list, skip_list):
    final_message.extend(complete_message[message_index:message_index + take])
    message_index += take + skip

print(''.join(final_message))
