
def walkToPt(target, point):
    fuel = 0
    while True:
        if point < target:
            point += 1
            fuel +=1 
        elif point > target:
            point -= 1
            fuel += 1
        else:
            return fuel
        


def main():
    with open("input.txt") as file:
        data = list(map(int, file.readline().split(",")))
        #data = [16,1,2,0,4,2,7,1,2,14]

    fuelCons = []
    for target in data:
        totalFuel = 0
        for point in data:
            totalFuel += walkToPt(target, point)
        fuelCons.append((target, totalFuel))
    
    print(min(fuelCons, key=lambda t: (t[1], -t[0])))
        


if __name__ == "__main__":
    main()