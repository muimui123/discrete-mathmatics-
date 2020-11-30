#Import files Part 2
import sys
if len(sys.argv) == 1:
	print "forgot input file name"
	exit(0)
filename = sys.argv[1]
file = open(filename)
files = file.readlines()

#Function
def push(array,element):
	array.insert(0,element)

def pop(array): 
	return array.pop(0)

#loop the string	
for line in files:
	#string = "6 6 * 2 7 * - 2 /"
	string = line.strip()
	print "input:", string
	input = string.split(" ")
	formula = []
	for i in input:
		if i not in "+-*/":
			push(formula,float(i))
		else:
			number2 = pop(formula)
			number1 = pop(formula)
			if i == "+":
				number = number1 + number2
			elif i == "-":
				number = number1 - number2
			elif i == "*":
				number = number1  * number2
			elif i == "/":
				number = number1 / number2	
			push(formula,number)
	print formula[0]
	

