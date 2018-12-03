def separate(line):
    l = line.split(' @ ')
    id = l[0]
    l2 = l[1].split(': ')
    origin = l2[0].split(',')
    area = l2[1].split('x')

    return {
        "id": id,
        "origin": (int(origin[0]), int(origin[1])),
        "area": (int(area[0]), int(area[1]))
    }

def claim(line):
    claimData = separate(line)
    claimResult = {}

    xrange = range(claimData["origin"][0], claimData["origin"][0] + claimData["area"][0])
    yrange = range(claimData["origin"][1], claimData["origin"][1] + claimData["area"][1])

    for y in yrange:
        for x in xrange:
            claimResult.update({(x, y): 1})

    return claimResult


def findOverlapCountInClaims(lines):
    claimResults = [claim(line) for line in lines]

    resultDict = claimResults.pop()

    for claimResult in claimResults:
        for point in claimResult.keys():
            if point in resultDict:
                newValue = resultDict[point] + claimResult[point]
                resultDict.update({ point: newValue })
            else:
                resultDict.update({ point: 1 })

    count = 0
    for key in resultDict.keys():
        if key in resultDict and resultDict[key] > 1:
            count += 1

    return count

def main():
    lines = open("./input.txt").readlines()
    print(findOverlapCountInClaims(lines))

main()
