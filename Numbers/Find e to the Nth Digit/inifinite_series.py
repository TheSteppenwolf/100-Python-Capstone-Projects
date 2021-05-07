'''
This code will get the value of e by following the sum of infinite series 1/n!
'''

def factorial(num, result=1):
	'''
	This functions returns the factorial of a given number
	'''
	if num == 0:
		return result
	return factorial(num-1, result*num)

def infinite_series(n):
	'''
	This code returns e following the sum of infinite series 1/n!
	'''
	e = 0
	for x in range(n):
		e += 1/factorial(x)
	return e

if __name__ == "__main__":
	# Variables
	# The value of e
	e = 0
	# The value of n which will approximate the value of e
	n = 0
	# Number of digits wanted
	digits = 0

	# Input
	n = int(input("Enter n: "))
	digits = int(input("Enter the number of digits wanted: "))

	# Process
	e = infinite_series(n)

	# Output
	print(f"e: %.{digits}f"%(e))