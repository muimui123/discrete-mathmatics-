import sys
if len(sys.argv) == 1:
	print "forgot input file name"
	exit(0)
filename = sys.argv[1]
file = open(filename)
files = file.readlines()


#show A
A = files[0].strip('\n').split(" ")
result = "A = {"
for index in range(len(A)):
	if index == len(A)-1:
		result += A[index]
	else:
		result += A[index] + ", "
result += "}"
print result

#showB 
B = files[1].strip('\n').split(" ")
result = "B = {"
for index in range(len(B)):
	if index == len(B)-1:
		result += B[index]
	else:
		result += B[index] + ", "
result += "}"
print result

#A intersects B
intersect = []
for x in B:
	if x in A:
		intersect.append(x)
result = "A intersect B = {"
for index in range(len(intersect)):
	if index == len(intersect)-1:
		result += intersect[index]
	else:
		result += intersect[index] + ", "
result += "}"
print result

#A union B
Union = A+B
for x in intersect:
	Union.remove(x)
result = "A Union B = {"
for index in range(len(Union)):
	if index == len(Union)-1:
		result += Union[index]
	else:
		result += Union[index] + ", "
result += "}"
print result

#A-B
Aminus = files[0].strip('\n').split(" ")
for x in Aminus:
	if x in B:
		Aminus.remove(x)
result = "A - B = {"
for index in range(len(Aminus)):
	if index == len(Aminus)-1:
		result += Aminus[index]
	else:
		result += Aminus[index] + ", "
result += "}"
print result


#B-A
Bminus = files[1].strip('\n').split(" ")
for x in Bminus:
	if x in A:
		Bminus.remove(x)
result = "B - A = {"
for index in range(len(Bminus)):
	if index == len(Bminus)-1:
		result += Bminus[index]
	else:
		result += Bminus[index] + ", "
result += "}"
print result


#AXB
crossA = []
for x in A:
	for y in B:
		crossA.append( "(" + x + "," + y  +")")
result = "A * B = {"
for index in range(len(crossA)):
	if index == len(crossA)-1:
		result += crossA[index]
	else:
		result += crossA[index] + ", "
result += "}"
print result


#BXA
crossB = []
for x in B:
	for y in A:
		crossB.append( "(" + x + "," + y  +")")
result = "B * A = {"
for index in range(len(crossB)):
	if index == len(crossB)-1:
		result += crossB[index]
	else:
		result += crossB[index] + ", "
result += "}"
print result





