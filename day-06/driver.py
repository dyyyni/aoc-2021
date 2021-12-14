import anglerFishMod

def main():
    with open("input.txt") as file:
        rawData = file.readline().split(",")
        data = list(map(int,[fish for fish in rawData]))
    
    fishPopulation = []
    [fishPopulation.append(anglerFishMod.anglerFish(fish)) for fish in data]

    babyCount = 0
    for i in range(80):
        for fish in fishPopulation:
            fish.reduceTimer()
            if fish.isTimeToRepro():
                babyCount += 1
        for i in range(babyCount):
            fishPopulation.append(anglerFishMod.anglerFish())
        babyCount = 0
                

    print(len(fishPopulation))

if __name__ == "__main__":
    main()