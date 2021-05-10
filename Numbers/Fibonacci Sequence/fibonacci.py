def list_fibonacci(max_num):
    '''
    Returns the fibonacci sequence as a list up to the max number wished
    '''
    # Saves the sequence | F0 = 0, F1 = 1
    sequence = [0, 1]
    # Starts the evaluation    
    for x in range(2, max_num):
        sequence.append(sequence[-1] + sequence[-2])
    # Returns the list
    return sequence

def gen_fibonacci(max_num):
    '''
    This function works as a generator and yields element by element of the Fibonacci sequence
    '''
    # F0 = 0, F1 = 1
    f1, f2 = 0, 1
    for x in range(max_num):
        # Yields the next value
        yield f1
        f1, f2 = f2, f1+f2

def fibonacci_recursive_onpoint(max_num, f1=0, f2=1):
    '''
    This function returns a single value corresponding at the position in the Fibonacci sequence
    '''
    # Ends the recursive function
    if max_num < 2:
        return f1
    # Continue to evaluate the next position of the sequence
    return fibonacci_recursive_onpoint(max_num-1, f2, f1+f2)

def fibonacci_recursive_topoint(max_num, sequence=[]):
    '''
    This functions return the entire sequence up to the position wanted by recursion.
    '''
    # Ends the recursive function
    if max_num == 2:
        return sequence
    # F0 = 0, F1 = 1    
    if len(sequence) == 0:
        sequence = [0, 1]
    # Evaluates the next position of the sequence
    sequence.append(sequence[-1]+sequence[-2])
    return fibonacci_recursive_topoint(max_num-1, sequence)

if __name__ == "__main__":
    # Variables
    max_sequence = 0
    
    # Input
    max_sequence = int(input("Number of elements of the Fibonacci sequence: "))

    # Process
    print()
    # list_fibonacci
    sequence = ", ".join(map(str, list_fibonacci(max_sequence)))
    print(f"Fibonacci sequence by list_fibonacci up to {max_sequence} numbers: {sequence}", end="\n\n")
    # gen_fibonacci
    gen = gen_fibonacci(max_sequence)
    print(f"Fibonacci sequence by gen_fibonacci up to {max_sequence} numbers: ", end="")
    for x in range(max_sequence):
        if x == max_sequence-1:
            print(next(gen), end="\n\n")
        else:
            print(f"{next(gen)}, ", end="")
    # fibonacci_recursive_onpoint
    print(f"Fibonacci sequence by fibonacci_recursive_onpoint at the {max_sequence} position: {fibonacci_recursive_onpoint(max_sequence)}", end="\n\n")
    # fibonacci_recursive_topoint
    sequence = ", ".join(map(str, fibonacci_recursive_topoint(max_sequence)))
    print(f"Fibonacci sequence by fibonacci_recursive_topoint up to {max_sequence} numbers: {sequence}", end="\n\n")

