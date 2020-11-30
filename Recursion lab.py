def sort205(p, r):
    if p < r: 
        q = divide(p,r)
		#call function
        sort205(p, q-1)
        sort205(q+1, r)

		
def divide(p, r): 
	x = A[r]
	i = p-1
	for j in range (p,r):
		if A[j] <= x: 
			i += 1
			#exchange
			tmp = A[i]
			A[i] = A[j]
			A[j] = tmp
	tmp = A[i+1]
	A[i+1] = A[r]
	A[r] = tmp
	return (i+1)

#error	
import sys
if len(sys.argv) == 1:
	print "forgot input file name"
	exit(0)
filename = sys.argv[1]
file = open(filename)
files = file.readlines()
A = []
A = [int(i)for i in files]
sort205(0,len(A)-1)
print A



