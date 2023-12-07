DEBUG_PRINTING = True
TESTING = False

from math import prod

def partOne(fi):
	with open(fi, "r") as f:
		times = [int(n) for n in ' '.join(f.readline().rstrip().split()).split(': ')[1].split(' ')]
		distances = [int(n) for n in ' '.join(f.readline().rstrip().split()).split(': ')[1].split(' ')]
	
	print(partOneHelper(times, distances))


def partOneHelper(t, d):
	waysToBeat = [0] * len(t)
	for i in range(len(t)):
		currentSpeed = 0
		for j in range(t[i]):
			if d[i] < (currentSpeed * (t[i] - j)):
				waysToBeat[i] += 1
			currentSpeed += 1
	
	return prod(waysToBeat)


def partTwo(fi):
	with open(fi, "r") as f:
		times = [int(''.join(f.readline().rstrip().split()).split(':')[1])]
		distances = [int(''.join(f.readline().rstrip().split()).split(':')[1])]
	
	print(partTwoHelper(times, distances))


def partTwoHelper(t, d):
	waysToBeat = [0] * len(t)
	for i in range(len(t)):
		currentSpeed = 0
		for j in range(t[i]):
			if d[i] < (currentSpeed * (t[i] - j)):
				waysToBeat[i] += 1
			currentSpeed += 1
	
	return prod(waysToBeat)
	

def main():
	if TESTING:
		fi = "test.txt"
	else:
		fi = "06.txt"
	
	partOne(fi)
	partTwo(fi)
	

def debugPrint(*s):
	if DEBUG_PRINTING:
		print(s)

main()