import math
import time
# returns the position of the item
def binary_search(list:list[int], item:int):

    low = 0 # first element position
    high = len(list) - 1 # last element position

    while low <= high:
        mid = math.floor((low + high)/2) # middle element position
        guess = list[mid]

        if guess == item:
            return mid # found it!
        if guess > item:
            high = mid -1 # look to the left
        else:
            low = mid + 1 # look to the right

    return None



if __name__ == "__main__":
    steps = 1
    numbers = [i for i in range(0,100 + 1)]

    print("Think of a number between 0 to 100 (don't show me 🙈)")
    time.sleep(2)
    low = 0
    high = len(numbers) -1
    foundElement = False

    while low <= high:
        mid = math.floor((low + high)/2)

        guess = numbers[mid]

        side_of_element = input(f"{steps}. Your element is {guess}? (y/n):")

        if side_of_element == "y":
            print(f"I FOUND IT!\nYour number is {guess}.")
            print(f"I found in {steps} steps")
            foundElement = True
            break
        
        side_of_element = input(f"Your element is greater than {guess}? (y/n):")
        
        if side_of_element == "y":
            print("\nLets look to the right\n")
            low = mid + 1

        else:
            print("\nLets look to the left\n")
            high = mid -1
        
        steps += 1

    if not foundElement:
        print("Oh man, i guess the number you've choosed its not between 0 and 100!")



    