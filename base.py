DEBUG_PRINTING = True
TESTING = True

def partOne(fi):
	with open(fi, "r") as f:
		for s in f:
			print()


def partTwo(fi):
	with open(fi, "r") as f:
		for s in f:
			print()
	

def main():
	if TESTING:
		fi = "test.txt"
	else:
		fi = "03.txt"
	
	partOne(fi)
	partTwo(fi)
	

def debugPrint(*s):
	if DEBUG_PRINTING:
		print(s)

main()