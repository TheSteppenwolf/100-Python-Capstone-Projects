'''
The code will generate Pi up any decimal wanted using the Leibniz Series.

Notice: take in mind that bigger the decimals wanted, the bigger the precision must be,
	for example, for 5 digits of Pi it is required a precision of 500000.
'''

# Required libraries
import datetime

# Fnctions
def leibniz(iterations):
	'''
	This functions return the value of pi given the precision wanted using the Leibniz series
	'''
	den = 0.0
	pi = 0.0
	for x in range(iterations):
		den = 2 * x + 1		
		if x % 2 == 0:			
			pi += 1 / den
		else:
			pi -= 1 / den
	# Notice that the series equals Pi/4
	return pi * 4

if __name__ == "__main__":
    # Variables
    # Max iterations wanted to upgrade the precision on finding Pi
    iterations = 0
    # Number of digits wanted
    n = 0
    # Value of Pi given n
    pi = 0.

    # Input    
    iterations = int(input("Please enter the precision for the calculation of Pi: "))
    n = int(input("Please enter the number of decimals you want: "))    

    # Process
    start_time = datetime.datetime.now()
    pi = leibniz(iterations)
    end_time = datetime.datetime.now()

    # Output    
    print(f"pi: %.{n}f" % (pi))    
    print(f"Tiempo de ejecución: {(end_time - start_time).total_seconds() * 10}ms")