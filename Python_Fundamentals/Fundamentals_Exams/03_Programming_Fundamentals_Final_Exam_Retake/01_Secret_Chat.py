message = input()

while True:
    line = input()
    if line == "Reveal":
        break
    parts = line.split(":|:")
    if parts[0] == "InsertSpace":
        idx = int(parts[1])
        message = message[:idx] + " " + message[idx:]
        print(message)
    elif parts[0] == "Reverse":
        sub = parts[1]
        pos = message.find(sub)
        if pos != -1:
            message = message[:pos] + message[pos + len(sub):] + sub[::-1]
            print(message)
        else:
            print("error")
    elif parts[0] == "ChangeAll":
        sub = parts[1]
        rep = parts[2]
        message = message.replace(sub, rep)
        print(message)

print(f"You have a new text message: {message}")
