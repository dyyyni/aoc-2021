
depthsRaw = open("input.txt", "r")
depths = []
try:
    [depths.append(int(x.strip())) for x in depthsRaw.readlines()]
except ValueError:
    pass
depthsRaw.close()

counter = 0
prev = 0
for depth in depths[1:]:
    if depth > depths[prev]:
        counter += 1
    prev +=1

print(counter)