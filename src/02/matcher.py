# returns 2 booleans
# first boolean for two chars
# second boolean for three chars
def count(line):
    sortedLine = ''.join(sorted(line))
    stringset = set([x for x in sortedLine])

    hasTwo = False
    hasThree = False

    for i in stringset:
        c = sortedLine.count(i)

        if c == 2:
            hasTwo = True
        elif c == 3:
            hasThree = True

        if hasTwo and hasThree:
            break

    return hasTwo, hasThree

def checksum(lines):
    countTwo = 0
    countThree = 0
    for line in lines:
        result = count(line)
        if result[0]:
            countTwo += 1

        if result[1]:
            countThree += 1

    return countTwo * countThree

def findDifference(a, b):
    limit = 9
    differCount = 0
    differIndexes = []
    for x in range(0, len(a)):
        if a[x] == b[x]:
            continue
        else:
            differCount += 1
            differIndexes.append(x)

            if differCount >= limit:
                break

    return differCount, differIndexes

def compare(lines):
    lineLists = [line.rstrip() for line in lines]
    count = 0

    for i in range (0, len(lineLists)):
        currentLine = lineLists[i]
        for j in range(i + 1, len(lineLists)):
            results = findDifference(currentLine, lineLists[j])
            if results[0] == 1:
                final = list(currentLine[:])
                del final[results[1][0]]
                return ''.join(final)

        count += 1

def main():
    lines = open("./input.txt").readlines()
    print('results: ' + compare(lines))

main()