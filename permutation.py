import sys
if len(sys.argv) == 1:
	print "forgot input file name"
	exit(0)
#input files	
filename = sys.argv[1]
file = open(filename)
files = file.readlines()

# creat array
Section = 0 
rice = []
meat = []
egg = []
gravy = []
count_star = 0

#loopf iles
for line in files: 
	line_strip = line.strip('\n')
	if line_strip == "***": 
		Section += 1 
	elif Section == 0: 
			rice.append(line_strip) 
	elif Section == 1: 
			meat.append(line_strip)
	elif Section == 2: 
			egg.append(line_strip)
	elif Section == 3: 
			gravy.append(line_strip)

combination = 0
for r in rice: 
	for m in meat: 
		for e in egg: 
			for g in gravy: 
				print r + " rice," + m + " meat," + e + " eggs," + g + " gravy" 
				combination += 1
				
print "=============="
print str(combination) + "Loco moco! Collect them all!"