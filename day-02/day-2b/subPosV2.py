with open("input.txt") as file:
    movesRaw = [move.strip().split(' ') for move in file.readlines()]
    moves = list((zip([x[0] for x in movesRaw], map(lambda n: int(n[1]), movesRaw))))

x = 0
y = 0 # down is positive
aim = 0

for move in moves:
    if move[0] == 'forward':
        x += move[1]
        y = y + aim*move[1]
    elif move[0] == 'up':
        aim -= move[1]
    elif move[0] == 'down':
        aim += move[1]

print(x,y)
print(x*y)