'''
	This code is planned to get the value of e up the Nth digit given using the formula: lim(1 + 1/n)^n,
	here as n approaches infinity we will be getting the value of e.
'''

def lim_e(n):
	'''
	The function return the value of e given n.	
	'''
	return pow(1 + 1/n, n)

if __name__ == "__main__":
	# The value of e
	e = 0
	# The value of n which will aproximate e
	n = 0
	# Number of digits wanted
	digits = 0

	# Input
	n = int(input("Enter n: "))
	digits = int(input("Enter the number of digits wanted: "))

	# Process
	e = lim_e(n)

	# Output
	print(f"e: %.{digits}f"%(e))