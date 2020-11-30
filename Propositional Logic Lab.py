import sys
if len(sys.argv) == 1:
	print "forgot input file name"
	exit(0)
filename = sys.argv[1]
file = open(filename)
files = file.readlines()
qwords = ["what","where","how","why","who","when"]
pronouns = ["he","she","it","they"]
for line in files:
	line = line.strip('\n')
	arr = line.split(" ")
	flag = False
	for words in arr:
	#detect pronouns
		if words.lower() in pronouns:
			print "NOT A STATEMENT"
			flag = True
	#detect ?
	if line[-1] == '?':
		print "NOT A STATEMENT"
	elif len(arr) == 1:
		print "NOT A STATEMENT"
	elif arr[0].lower() in qwords:
		print "NOT A STATEMENT"
	#correct
	elif not flag:
		print "STATEMENT"
		
			


