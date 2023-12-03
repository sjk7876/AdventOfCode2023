SYMBOLS = "!@#$%^&*()_+=-`~/"

def partOne():
	overall = []
	# with open("test.txt", "r") as f:
	with open("03.txt", "r") as f:
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
				found, num, length = getNum(table, i, j)

				if found:
					nums += int(num)
					j += length
			j += 1
	
	return nums


def getNum(table, i, j):
	numCols = len(table[0])
	lengthToSkip = 0
	num = ""

	if not checkNbrs(table, i, j):
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


def checkNbrs(table, i, j):
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


def partTwo():
	with open("test.txt", "r") as f:
		print()
	

partOne()
partTwo()