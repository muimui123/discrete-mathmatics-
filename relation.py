import sys
if len(sys.argv) == 1:
	print "forgot input file name"
	exit(0)
#input files	
filename = sys.argv[1]
file = open(filename)
files = file.readlines()

# create array
title = [] 
authors = [] 
genres = [] 
year = []

for i in files:
	words = i.strip().split("|") 
	title.append (words[0]) 
	authors.append (words[1]) 
	genres.append (words[2]) 
	year.append (words[3])

#loop
while True:
	print "Select books based on?"
	print "[T]itle"
	print "[A]uthor"
	print "[G]enre"
	print "[Y]ear"
	print  "E[X]it Program"
	
	#input
	t = raw_input()
	if t == "t":
		print "Please enter title:"
		type = raw_input()
		count=0
		for i in range(0, len(title)):
			if type.lower() in title[i].lower():
				print "(", genres[i], ")", title[i], "by", authors[i], year[i]
				count +=1
		print count, " records retrieved."			
	if t == "g":
		print "Please enter genre:"
		type = raw_input()	
		count=0
		for i in range(0, len(genres)):
			if type.lower() in genres[i].lower():
				print "(", genres[i], ")", title[i], "by", authors[i], year[i]
				count +=1
		print count, " records retrieved."			
	if t == "a":
		print "Please enter authors:"
		type = raw_input()	
		count=0
		for i in range(0, len(authors)):
			if type.lower() in authors[i].lower():
				print "(", genres[i], ")", title[i], "by", authors[i], year[i]
				count +=1
		print count, " records retrieved."	
	if t == "y":
		print "Please enter year:"
		type = raw_input()	
		count=0
		for i in range(0, len(year)):
			if type in year[i]:
				print "(", genres[i], ")", title[i], "by", authors[i], year[i]
				count +=1
		print count, " records retrieved."	
	if t == "x":
		break