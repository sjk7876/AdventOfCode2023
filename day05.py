DEBUG_PRINTING = True
TESTING = False

def partOne(fi):
	with open(fi, "r") as f: 
		# switch to storing how to generate each number instead of generating every dictionary
		dictsList = [{}, {}, {}, {}, {}, {}, {}]
		seeds = [int(n) for n in f.readline().rstrip().split(': ')[1].split()]
		f.readline()

		for i in range(7):
			f.readline()

			while True:
				line = f.readline().rstrip()
				if not line:
					break
				line = [int(n) for n in line.split()]
				for j in range(line[2]):
					dictsList[i][line[1] + j] = line[0] + j
			print("done")
			
	print(partOneHelper(seeds, dictsList))


def partOneHelper(seeds, maps):
	results = []
	for seed in seeds:
		current = seed
		for i in range(len(maps)):
			if current in maps[i]:
				current = maps[i][current]
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