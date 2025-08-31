stops = input()

while True:
    line = input()
    if line == "Travel":
        break
    parts = line.split(":")
    cmd = parts[0]
    if cmd == "Add Stop":
        index = int(parts[1])
        string = parts[2]
        if 0 <= index <= len(stops):
            stops = stops[:index] + string + stops[index:]
        print(stops)
    elif cmd == "Remove Stop":
        start = int(parts[1])
        end = int(parts[2])
        if 0 <= start <= end < len(stops):
            stops = stops[:start] + stops[end + 1:]
        print(stops)
    elif cmd == "Switch":
        old = parts[1]
        new = parts[2]
        if old in stops:
            stops = stops.replace(old, new)
        print(stops)

print(f"Ready for world tour! Planned stops: {stops}")
