

with open("input.txt") as file:
    movesRaw = [move.strip().split(' ') for move in file.readlines()]
    movesInt = map(lambda n: int(n[1]), movesRaw)
    moves = list((zip([x[0] for x in movesRaw], movesInt)))

x = 0
y = 0 # down is positive

for move in moves:
    if move[0] == 'forward':
        x += move[1]
    elif move[0] == 'up':
        y -= move[1]
    elif move[0] == 'down':
        y += move[1]

print(x,y)
print(x*y)