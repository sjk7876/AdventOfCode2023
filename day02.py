MAX = {'red': 12, 'green': 13, 'blue': 14}

def handlePartOne(row):
    id = int(row[1])

    row = row[2:]

    for i in range(0, len(row) - 1, 2):
        if int(row[i]) > MAX[row[i+1]]:
            return 0
    
    return id


def partOne():
    sum = 0

    with open("02.txt", "r") as f:
        for s in f:
            row = s.replace(',', '').replace(':', '').replace(';', '').split()
            sum += handlePartOne(row)

    print(sum)


def handlePartTwo(row):
    row = row[2:]

    MIN = {'red': 0, 'green': 0, 'blue': 0}

    for i in range(0, len(row) - 1, 2):
        if int(row[i]) > MIN[row[i+1]]:
            MIN[row[i+1]] = int(row[i])
    
    power = MIN['red'] * MIN['green'] * MIN['blue']
    return power


def partTwo():
    sum = 0

    with open("02.txt", "r") as f:
        for s in f:
            row = s.replace(',', '').replace(':', '').replace(';', '').split()
            sum += handlePartTwo(row)

    print(sum)


partOne()
partTwo()