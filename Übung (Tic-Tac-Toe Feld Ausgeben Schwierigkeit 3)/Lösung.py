ttt = [
    ["x", "o", "x"],
    [" ", "x", " "],
    ["o", "x", "o"]
]

print("+---+")

for row in ttt:
    print('|', end='')
    print(f'{row[0]}{row[1]}{row[2]}', end='')
    print('|')

print("+---+")
