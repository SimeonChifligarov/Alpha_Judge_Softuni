message = input()

while True:
    line = input()
    if line == "Decode":
        break
    parts = line.split("|")
    if parts[0] == "Move":
        n = int(parts[1])
        message = message[n:] + message[:n]
    elif parts[0] == "Insert":
        index = int(parts[1])
        value = parts[2]
        message = message[:index] + value + message[index:]
    elif parts[0] == "ChangeAll":
        substring = parts[1]
        replacement = parts[2]
        message = message.replace(substring, replacement)

print(f"The decrypted message is: {message}")
