DEBUG_PRINTING = False
TESTING = False

def partOne(fi):
	with open(fi, "r") as f: 
		rangesList = [[], [], [], [], [], [], []]
		seeds = [int(n) for n in f.readline().rstrip().split(': ')[1].split()]
		f.readline()
		for i in range(7):
			f.readline()

			while True:
				line = f.readline().rstrip()
				if not line:
					break
				line = [int(n) for n in line.split()]
				rangesList[i].append(line)
			
	print(partOneHelper(seeds, rangesList))


def partOneHelper(seeds, maps):
	results = []
	for seed in seeds:
		current = seed
		nex = current

		for i in range(len(maps)): # each mapping (seed to soil)
			for j in range(len(maps[i])): # specifics (50 98 2)
				if current >= maps[i][j][1] and current < maps[i][j][1] + maps[i][j][2]:
					nex = (current - maps[i][j][1]) + maps[i][j][0]
					debugPrint('in', current, nex)
					break
				debugPrint('in', current, nex)
			debugPrint('out', current, nex, '\n')
			current = nex
		results.append(current)
	
	return min(results)


def partTwo(fi):
	with open(fi, "r") as f:
		for s in f:
			print(end='')
	

def main():
	if TESTING:
		fi = "test.txt"
	else:
		fi = "05.txt"
	
	partOne(fi)
	partTwo(fi)
	

def debugPrint(*s):
	if DEBUG_PRINTING:
		print(s)

main()