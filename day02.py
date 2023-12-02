MAX = {'red': 12, 'green': 13, 'blue': 14}

def handlePartOne(row):
    id = int(row[1])

    row = row[2:]

    for i in range(0, len(row) - 1, 2):
        if int(row[i]) > MAX[row[i+1]]:
            # print(id, "bad", row[i], row[i+1])
            return 0
    
    # print(id, "good")
    return id, max


def partOne():
    sum = 0

    with open("02.txt", "r") as f:
        for s in f:
            row = s.replace(',', '').replace(':', '').replace(';', '').split()
            sum += handlePartOne(row)

    print(sum)


partOne()
