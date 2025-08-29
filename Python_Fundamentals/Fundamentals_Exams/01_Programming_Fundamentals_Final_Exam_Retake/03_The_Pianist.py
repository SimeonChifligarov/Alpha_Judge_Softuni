n = int(input())

pieces = {}
for _ in range(n):
    piece, composer, key = input().split("|")
    pieces[piece] = [composer, key]
while True:
    line = input()
    if line == "Stop":
        break
    parts = line.split("|")
    if parts[0] == "Add":
        piece, composer, key = parts[1], parts[2], parts[3]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif parts[0] == "Remove":
        piece = parts[1]
        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif parts[0] == "ChangeKey":
        piece, new_key = parts[1], parts[2]
        if piece in pieces:
            pieces[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, (composer, key) in pieces.items():
    print(f"{piece} -> Composer: {composer}, Key: {key}")
