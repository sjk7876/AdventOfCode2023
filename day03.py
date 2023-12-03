import copy

DEBUG_PRINTING = True
TESTING = True

SYMBOLS = "!@#$%^&*()_+=-`~/"

def partOne(fi):
	overall = []
	with open(fi, "r") as f:
		for s in f:
			line = []
			for l in s.rstrip():
				line.append(l)
			
			overall.append(line)

	print(partOneHelper(overall))


def partOneHelper(table):
	numCols = len(table[0])
	numRows = len(table)

	nums = 0

	for i in range(numRows):
		j = 0
		while j < numCols:
			if table[i][j].isdigit():
				found, num, length = getNumOne(table, i, j)

				if found:
					nums += int(num)
					j += length
			j += 1
	
	return nums


def getNumOne(table, i, j):
	numCols = len(table[0])
	lengthToSkip = 0
	num = ""

	if not checkNbrsOne(table, i, j):
		return False, 0, 0

	tempJ = j
	while tempJ >= 0 and tempJ <= numCols - 1:
		if table[i][tempJ] == "." or table[i][tempJ] in SYMBOLS:
			break

		num = table[i][tempJ] + num
		tempJ -= 1
		
	tempJ = j + 1
	while tempJ >= 0 and tempJ <= numCols - 1:
		if table[i][tempJ] == "." or table[i][tempJ] in SYMBOLS:
			break
		
		num += table[i][tempJ]
		lengthToSkip += 1
		tempJ += 1
	
	return True, num, lengthToSkip	


def checkNbrsOne(table, i, j):
	numCols = len(table[0])
	numRows = len(table)

	if i > 0:                           # check left
		if table[i-1][j] in SYMBOLS:
			return True

		if j > 0:                       # check up left
			if table[i-1][j-1] in SYMBOLS:
				return True
		if j < numCols - 1:             # check down left
			if table[i-1][j+1] in SYMBOLS:
				return True

	if i < numRows - 1:					# check right
		if table[i+1][j] in SYMBOLS:
			return True

		if j > 0:						# check up right
			if table[i+1][j-1] in SYMBOLS:
				return True
		if j < numCols - 1:				# check down right
			if table[i+1][j+1] in SYMBOLS:
				return True

	if j > 0:							# check up
		if table[i][j-1] in SYMBOLS:
			return True
	if j < numCols - 1:					# check down
		if table[i][j+1] in SYMBOLS:
			return True
	
	return False


def partTwo(fi):
	overall = []
	with open(fi, "r") as f:
		for s in f:
			line = []
			for l in s.rstrip():
				line.append(l)
			
			overall.append(line)

	print(partTwoHelper(overall))


def partTwoHelper(table):
	numCols = len(table[0])
	numRows = len(table)
	
	nums = 0

	for i in range(numRows):
		j = 0
		while j < numCols:
			if table[i][j] == "*":
				debugPrint('* found', i, j)
				found, num, newTable = checkNbrsTwo(table, i, j)

				if found:
					table = newTable
					nums += num
				debugPrint('out')
				# for x in table:
				# 	print(x)
				debugPrint()
			j += 1
			
	return nums


def getNumTwoReplace(table, i, j):
	numCols = len(table[0])
	num = ""

	tempJ = j
	while tempJ >= 0 and tempJ <= numCols - 1:
		if table[i][tempJ] == "." or table[i][tempJ] in SYMBOLS:
			break
		
		num = table[i][tempJ] + num
		table[i][tempJ] = "."
		tempJ -= 1
		
	tempJ = j + 1
	while tempJ >= 0 and tempJ <= numCols - 1:
		if table[i][tempJ] == "." or table[i][tempJ] in SYMBOLS:
			break
		
		num += table[i][tempJ]
		table[i][tempJ] = "."
		tempJ += 1
		for x in range(numCols):
			debugPrint(table[x])

	debugPrint('ee',num, i, j, table[i][j], table[i][j+1], table[i][j-1])
	debugPrint()
	
	return int(num)


def checkNbrsTwo(table, i, j):
	debugPrint()
	numCols = len(table[0])
	numRows = len(table)

	tempTable = copy.deepcopy(table)

	total = 0
	nums = []

	if i > 0:                           # check left
		if tempTable[i-1][j].isdigit():
			total += 1
			debugPrint('left')
			nums.append(getNumTwoReplace(tempTable, i-1, j))

		if j > 0 and tempTable[i-1][j-1].isdigit():
			total += 1
			debugPrint('up left')
			nums.append(getNumTwoReplace(tempTable, i-1, j-1))

		if j < numCols - 1 and tempTable[i-1][j+1].isdigit():
			total += 1
			debugPrint('down left')
			nums.append(getNumTwoReplace(tempTable, i-1, j+1))

	if i < numRows - 1:					# check right
		if tempTable[i+1][j].isdigit():
			total += 1
			debugPrint('right')
			nums.append(getNumTwoReplace(tempTable, i+1, j))

		if j > 0 and tempTable[i+1][j-1].isdigit():
			total += 1
			debugPrint('up right')
			nums.append(getNumTwoReplace(tempTable, i+1, j-1))

		if j < numCols - 1 and tempTable[i+1][j+1].isdigit():
			total += 1
			debugPrint('down right', i+1, j+1, tempTable[i+1][j+1])
			nums.append(getNumTwoReplace(tempTable, i+1, j+1))

	if j > 0 and tempTable[i][j-1].isdigit():
		total += 1
		debugPrint('up')
		nums.append(getNumTwoReplace(tempTable, i, j-1))

	if j < numCols - 1 and tempTable[i][j+1].isdigit():
		total += 1
		debugPrint('down')
		nums.append(getNumTwoReplace(tempTable, i, j+1))
	
	
	if total == 2:
		debugPrint("leaving", total, nums)
		table = copy.deepcopy(tempTable)
		return True, nums[0] * nums[1], table
	
	return False, 0, table


def debugPrint(*s):
	if DEBUG_PRINTING:
		print(s)
	

def main():
	if TESTING:
		fi = "test.txt"
	else:
		fi = "03.txt"
	
	partOne(fi)
	partTwo(fi)


main()