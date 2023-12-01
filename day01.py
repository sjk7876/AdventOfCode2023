'''
Solution for Day 1 of Advent Of Code 2023
'''

def getNum(s, direction):
    for letter in s[::direction]:
        if letter.isdigit():
            return letter
    return "0"


def main():
    total = 0

    with open("01.txt", "r") as f:
        for s in f:
            total += int("" + getNum(s, 1) + getNum(s, -1))    

    print(total)

main()