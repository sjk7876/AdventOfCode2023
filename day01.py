'''
Solution for Day 1 of Advent Of Code 2023
'''

numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def getNumPartOne(s, direction):
    for letter in s[::direction]:
        if letter.isdigit():
            return letter
    
    return "0"


def partOne():
    total = 0

    with open("01.txt", "r") as f:
        for s in f:
            total += int("" + getNumPartOne(s, 1) + getNumPartOne(s, -1))    

    print(total)


def getNumPartTwo(s, direction):
    for letter in s[::direction]:
        if letter.isdigit():
            return letter
    
    return "0"


def getNumForwardPartTwo(s):
    first_index = len(s)
    first_val = 0
    for i in range (len(s)):
        if s[i].isdigit():
            first_index = i
            first_val = int(s[i])
            break
    
    for num in numbers:
        first_word = s.find(num)
        if first_word != -1 and first_word < first_index:
            first_index = first_word
            first_val = numbers[num]
    
    return str(first_val)
    

def getNumBackwardPartTwo(s):
    last_index = 0
    last_val = 0
    for i in range(len(s)-1, -1, -1):
        if s[i].isdigit():
            last_index = i
            last_val = int(s[i])
            break
    
    for num in numbers:
        last_word = s.rfind(num)
        if last_word != -1 and last_word > last_index:
            last_index = last_word
            last_val = numbers[num]
    
    return str(last_val)


def partTwo():
    total = 0

    with open("01.txt", "r") as f:
        for s in f:
            total += int(getNumForwardPartTwo(s) + getNumBackwardPartTwo(s))

    print(total)

partOne()
partTwo()