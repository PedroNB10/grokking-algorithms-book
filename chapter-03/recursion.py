def countdown(i):
    print(i)

    if i <= 0: # base case
        return 
    countdown(i-1) # recursive case
    

if __name__ == "__main__":
    countdown(10)