import statistics
with open("input.txt") as file:
    binData = [list(dp.strip()) for dp in file.readlines()]

groupedByOrder = list((zip(*binData)))
gammaRate = ""
for set in groupedByOrder:
    gammaRate += statistics.mode(set)

epsilonRate = ""
for bit in gammaRate:
    if bit == "1":
        epsilonRate += "0"
    else:
        epsilonRate += "1"

print(gammaRate)
print(epsilonRate)

print(int(gammaRate,2)*int(epsilonRate,2))