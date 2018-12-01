import itertools

def calibrate(sequence):
    return sum([int(part) for part in sequence.split(',')])

def calibrateSame(sequence):
    current = 0
    numberList = set([0])

    splitSequence = [int(part) for part in sequence.split(',')]

    for num in itertools.cycle(splitSequence):
        current += num

        if current in numberList:
            return current
        else:
            numberList.add(current)

sequence = ','.join(open("./input.txt").readlines())
print(calibrateSame(sequence))