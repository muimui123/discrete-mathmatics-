#part1 
def drawRow(numSpaces, numStars):
	print " " * numSpaces + "*" * numStars
drawRow(5,1)
drawRow(2,8)
drawRow(0,3)

#part2
def drawPyramid(height): 
	for i in range (height):
		print(" "*(height-i-1)+"*"*(2*i+1))
drawPyramid(5)
drawPyramid(3)	

#Extra Credit
def drawInvertedPyramid(height):
	for i in reversed(range(height)):
		print(" "*(height-i-1) + "*"*(2*i+1))

#part3
import sys
if len(sys.argv) == 1:
	print "ERROR: Please supply command-line parameter"
	exit(0)	
n = int(sys.argv[1])
if n < 0:
	print "ERROR: Number must be non-negative"
	exit(0)	
drawPyramid(n)
drawInvertedPyramid(n)

