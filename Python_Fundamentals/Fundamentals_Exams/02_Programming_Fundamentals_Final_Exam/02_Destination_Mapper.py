import re

s = input()
destinations = [m[1] for m in re.findall(r'([=/])([A-Z][A-Za-z]{2,})\1', s)]

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {sum(len(d) for d in destinations)}")
