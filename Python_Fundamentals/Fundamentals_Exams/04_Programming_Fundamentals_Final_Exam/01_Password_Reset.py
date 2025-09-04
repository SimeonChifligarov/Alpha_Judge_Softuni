password = input()

while True:
    line = input()
    if line == "Done":
        break
    parts = line.split()
    if parts[0] == "TakeOdd":
        password = "".join(password[i] for i in range(1, len(password), 2))
        print(password)
    elif parts[0] == "Cut":
        index = int(parts[1])
        length = int(parts[2])
        password = password[:index] + password[index + length:]
        print(password)
    elif parts[0] == "Substitute":
        sub = parts[1]
        rep = parts[2]
        if sub in password:
            password = password.replace(sub, rep)
            print(password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {password}")
