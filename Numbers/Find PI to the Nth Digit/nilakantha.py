'''
The code will generate Pi up any decimal wanted using the Nilakantha Series.
Notice: take in mind that bigger the decimals wanted, the bigger the precision must be,
	for example, for 5 digits of Pi it is required a precision of 50.
'''

# Required libraries
import datetime

# Fnctions
def nilakantha(iterations):
    '''
    This functions return the value of pi given the precision wanted using the Nilakantha series
    '''
    den = 0.0
    pi = 0.0
    for x in range(iterations):
        if x == 0:
            pi += 3
        else:
            den = (2*x) * (2*x + 1) * (2*x + 2)		
            if x % 2 == 0:			
                pi -= 4 / den
            else:
                pi += 4 / den	
    return pi

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
    pi = nilakantha(iterations)
    end_time = datetime.datetime.now()

    # Output    
    print(f"pi: %.{n}f" % (pi))    
    print(f"Tiempo de ejecución: {(end_time - start_time).total_seconds() * 10}ms")