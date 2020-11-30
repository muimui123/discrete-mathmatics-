import sys
if len(sys.argv) == 1:
	print "forgot input file name"
	exit(0)
filename = sys.argv[1]
file = open(filename)
files = file.readlines()
nums = 0
for line in files:
	for words in line:
		if words == '8':
			nums += 1
print "Eights:" + str(nums)

	
