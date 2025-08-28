username = input()
while True:
    line = input()
    if line == "Registration":
        break
    parts = line.split()
    if parts[0] == "Letters":
        if parts[1] == "Lower":
            username = username.lower()
        elif parts[1] == "Upper":
            username = username.upper()
        print(username)
    elif parts[0] == "Reverse":
        if len(parts) >= 3 and parts[1].isdigit() and parts[2].isdigit():
            start = int(parts[1])
            end = int(parts[2])
            if 0 <= start < len(username) and 0 <= end < len(username):
                s = min(start, end)
                e = max(start, end)
                print(username[s:e + 1][::-1])
    elif parts[0] == "Substring":
        substr = line.split(' ', 1)[1].split(' ', 1)[1] if len(parts) > 2 else line.split(' ', 1)[1].split(' ', 1)[0]
        if substr in username:
            username = username.replace(substr, "", 1)
            print(username)
        else:
            print(f"The username {username} doesn't contain {substr}.")
    elif parts[0] == "Replace":
        ch = parts[1]
        username = username.replace(ch, "-")
        print(username)
    elif parts[0] == "IsValid":
        ch = parts[1]
        if ch in username:
            print("Valid username.")
        else:
            print(f"{ch} must be contained in your username.")
