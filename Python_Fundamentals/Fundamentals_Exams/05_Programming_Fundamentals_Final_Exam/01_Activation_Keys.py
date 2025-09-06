key = input()

while True:
    line = input()
    if line == "Generate":
        break
    parts = line.split(">>>")
    if parts[0] == "Contains":
        sub = parts[1]
        if sub in key:
            print(f"{key} contains {sub}")
        else:
            print("Substring not found!")
    elif parts[0] == "Flip":
        mode, start, end = parts[1], int(parts[2]), int(parts[3])
        segment = key[start:end]
        segment = segment.upper() if mode == "Upper" else segment.lower()
        key = key[:start] + segment + key[end:]
        print(key)
    elif parts[0] == "Slice":
        start, end = int(parts[1]), int(parts[2])
        key = key[:start] + key[end:]
        print(key)

print(f"Your activation key is: {key}")
