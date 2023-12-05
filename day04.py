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
	with open(fi, "r") as f:
		for s in f:
			print(end='')
	

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