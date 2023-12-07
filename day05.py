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

		for i in range(len(maps)): # each mapping (seed to soil)
			for j in range(len(maps[i])): # specifics (50 98 2)
				if current >= maps[i][j][1] and current < maps[i][j][1] + maps[i][j][2]:
					current = (current - maps[i][j][1]) + maps[i][j][0]
					break

		results.append(current)
	
	return min(results)


def partTwo(fi):
	with open(fi, "r") as f: 
		rangesList = [[], [], [], [], [], [], []]

		seedsPre = [int(n) for n in f.readline().rstrip().split(': ')[1].split()]
		seeds = []

		for i in range(0, len(seedsPre) - 1, 2):
			seeds.extend([seedsPre[i] + j for j in range(seedsPre[i + 1])])
		# print(seeds)

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