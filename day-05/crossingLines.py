# Needed help for this one. Thanks mebeim! https://github.com/mebeim/aoc
from typing import DefaultDict


def lineFinder(ax,ay, bx,by):
    '''
    Takes (x1,y1)->(x2,y2) and finds the straight lines.
    Returns coordinates in the straight lines.
    '''
    # Fixed x -> Vertical line.
    if ax == bx:
        for y in range(min(ay,by), max(ay,by) + 1):
            yield ax,y

    # Fixed y -> Horizontal line.
    if ay == by:
        for x in range(min(ax,bx), max(ax,bx) + 1):
            yield x, ay

def autorange(a, b):
    if a > b:
        yield from range(a, b - 1, -1)
    yield from range(a, b + 1)

def diag(ax,ay, bx,by):
    if ax != bx and ay != by:
        yield from zip(autorange(ax,bx), autorange(ay,by))

def main():
    # Parse the input into [(x1,y1),(x2,y2)]
    with open("input.txt") as file:
        lines = []
        for rawLine in file.readlines():
            a,b = rawLine.split("->")
            ax,ay = map(int, a.split(","))
            bx,by = map(int, b.split(","))
            lines.append((ax,ay, bx,by))

    # a dictionary that just counts the times points in cartesian 
    # space have been visited by the possibly intersecting lines
    gridDict = DefaultDict(int)
    for ax,ay, bx,by in lines:
        for x,y in lineFinder(ax,ay, bx,by):
            gridDict[x,y] += 1
    
    overLapA = sum(x > 1 for x in gridDict.values())

    print("Part A: ", overLapA)

    for line in lines:
        for point in diag(*line):
            gridDict[point] += 1
    
    overLapB = sum(x > 1 for x in gridDict.values())

    print("Part B: ", overLapB)
    
if __name__ == "__main__":
    main()