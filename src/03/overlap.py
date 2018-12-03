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

    return (claimData['id'], claimResult)

def createClaimsData(lines):
    claimResults = [claim(line) for line in lines]

    resultDict = claimResults.pop()[1]

    for claimResult in claimResults:
        claimResultDict = claimResult[1]
        for point in claimResultDict.keys():
            if point in resultDict:
                newValue = resultDict[point] + claimResultDict[point]
                resultDict.update({ point: newValue })
            else:
                resultDict.update({ point: 1 })

    return resultDict

def findOverlapCountInClaims(lines):
    claimsData = createClaimsData(lines)

    count = 0
    for key in claimsData.keys():
        if key in claimsData and claimsData[key] > 1:
            count += 1

    return count

def findClaimWithoutOverlaps(lines):
    claimsResults = createClaimsData(lines)
    claims = [claim(line) for line in lines]

    for c in claims:
        count = 0
        cData = c[1]
        for point in cData.keys():
            if claimsResults[point] > 1:
                count += 1

        if count == 0:
            return c[0]

    return 'Not Found'

def part1():
    lines = open("./input.txt").readlines()
    print(findOverlapCountInClaims(lines))

def part2():
    lines = open("./input.txt").readlines()
    print(findClaimWithoutOverlaps(lines))

# part1()
# part2()