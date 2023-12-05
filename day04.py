DEBUG_PRINTING = True
TESTING = False

def partOne(fi):
	total = 0
	with open(fi, "r") as f:
		for s in f:
			total += partOneHelper(s.rstrip().replace('  ', ' ').split(' ')[2:])
	
	print(total)


def partOneHelper(arr):
	split = arr.index('|')
	winningNums = arr[:split]
	ourNums = arr[split+1:]
	total = 0

	for x in ourNums:
		if x in winningNums:
			total += 1
	
	if total > 0:
		return 2**(total-1)
	return 0


def partTwo(fi):
	cards = []
	with open(fi, "r") as f:
		for s in f:
			cards.append(' '.join(s.rstrip().split()).split(': ')[1].split())
	print(partTwoHelper(cards))


def partTwoHelper(cards):
	vals = [1] * len(cards)
	
	for i in range(len(cards)):
		split = cards[i].index('|')
		winningNums = [int(n) for n in cards[i][:split]]
		ourNums = [int(n) for n in cards[i][split+1:]]
		won = len(set(winningNums).intersection(set(ourNums)))

		for j in range(i + 1, i + 1 + won):
			vals[j] += vals[i]

	return sum(vals)
	

def main():
	if TESTING:
		fi = "test.txt"
	else:
		fi = "04.txt"
	
	partOne(fi)
	partTwo(fi)
	

def debugPrint(*s):
	if DEBUG_PRINTING:
		print(s)

main()