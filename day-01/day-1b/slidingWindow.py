def slidingWindow(list, window):
    n = len(list)
    if n < window:
        print("invalid")
        return -1

    windowSumOne = sum(list[:window])
    counter = 0
    for i in range(n - window):
        windowSumTwo = windowSumOne - list[i] + list[i+window]
        if windowSumTwo > windowSumOne:
            counter +=1
        windowSumOne = windowSumTwo
    return counter

def main():
    depthsRaw = open("input.txt", "r")
    depths = []
    try:
        [depths.append(int(x.strip())) for x in depthsRaw.readlines()]
    except ValueError:
        pass
    depthsRaw.close()

    print(slidingWindow(depths, 3))

main()