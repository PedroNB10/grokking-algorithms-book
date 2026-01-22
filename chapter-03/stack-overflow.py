# stack_overflow_example.py

def overflow(n=0):
    # Print occasionally so you can see progress without flooding the console
    if n % 100 == 0:
        print("depth:", n)
    return overflow(n + 1)  # No base case -> infinite recursion

overflow()
