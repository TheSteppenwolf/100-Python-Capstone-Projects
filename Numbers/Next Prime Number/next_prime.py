'''
This program has functions that will show prime numbers as long as the user wants it
'''
def trial_primenumber(num):
    '''
    This function returns wether the number is prime or not as a bool:
        If True, the number is prime
        else, the number isn't prime
    '''
    is_prime = True
    # Validates the condition for prime to be greater than 1
    if num == 1:
        is_prime = False
    # Makes the evaluation for all numbers except for 1 and the number itself
    for x in range(2, num):
        if num % x == 0:
            is_prime = False
    return is_prime

if __name__ == "__main__":
    # Variables
    # Numbber to evaluate if prime
    num = 2
    # Helps to evaluate if the user want other prime number
    want_other = ""

    # Process and output
    while(True):        
        if trial_primenumber(num):
            # Prints the next prime number
            if num == 2:
                print(f"The first prime number: {num}")
            else:
                print(f"The next prime number: {num}")
            # Validates the input of correct data
            while(True):
                 want_other = input("Do you want the next prime number? (Y/N): ").upper()
                 if want_other == "Y" or want_other == "N":
                     break
                 print("Error: You have not entered a valid input.")
            # Evaluates if the program finishes
            if want_other == "N":
                break
        # Sums by one the number to evaluate if prime
        num += 1

        
