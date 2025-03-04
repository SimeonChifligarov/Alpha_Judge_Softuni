input_str = input()

dig_from_complete_message = []
complete_message = []

for el in input_str:
    if el.isdigit():
        dig_from_complete_message.append(int(el))
    else:
        complete_message.append(el)

take_list = dig_from_complete_message[0::2]
skip_list = dig_from_complete_message[1::2]

final_message = []
message_index = 0

for take, skip in zip(take_list, skip_list):
    final_message.extend(complete_message[message_index:message_index + take])
    message_index += take + skip

print(''.join(final_message))
