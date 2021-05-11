'''
This program contains functions to calculate a prime factorization to a given number.
'''
def get_factor_tuples(prime_factors):
    '''
    This function returns a list of tuples from a list of prime factos to simulate the visualization of the syntax:
        (base, exponent)
    '''
    # Will save the final list of tuples
    tuples_list = []
    # It will help at the momento of evaluation of the quantity of a single element at the list.
    past = 0
    # Generates the tuples and saves them into the list
    for x in prime_factors:
        # If the last number evaluated is the same of this one, then it omits it.
        if x == past:
            continue
        tuples_list.append((x, prime_factors.count(x)))
        past = x
    # Returns the tuple list
    return tuples_list

def trial_primefactor(num):
    '''
    The function returns a list with the prime factors of a given number by the method of Trial Division.
    Each element of the list are tuples which follows the syntax:
        (base, exponent)
    '''
    # Will save the prime factors not converted to the syntax (base, exponent)
    prime_factors = []
    # Refers to the starting point to evaluate
    x = 2
    # Validation for 0 or negative numbers
    if num < 1:
        return []
    # Evaluates all factors
    while(num != 1):
        # If is an even divition, proceed to save x into the list
        if num % x == 0:        
            num /= x
            prime_factors.append(x)
        else:            
            x += 1  
    # Returns the list of factors converted into the syntax (base, exponent)
    return get_factor_tuples(prime_factors)

if __name__ == "__main__":
    # Variables
    # Number to factorize
    num = 0
    # Will save the list of tuples with the factors
    factors = []

    # Input
    num = int(input("Enter the number to factorize: "))

    # Process
    factors = trial_primefactor(num)

    # Output
    print(f"The factors for {num} are: ", end="")
    if len(factors) > 0:
        for factor in factors:
            if factor == factors[-1]:
                print(f"{factor[0]}^{factor[1]}.")
            else:
                print(f"{factor[0]}^{factor[1]} * ", end="")
    else:
        print(" This number does not have prime factors.")
