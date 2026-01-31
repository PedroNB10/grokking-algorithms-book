import math

def recursive_sum_practice(arr:list):

    if len(arr) == 0:
        return 0
    
    first = arr.pop(0)
    
    return first + sum(arr)

# 4.1 Write out the code for the earlier sum function.
def recursive_sum(arr: list):
    if len(arr) == 0:
        return 0
    return arr[0] + recursive_sum(arr[1:])


# 4.2 Write a recursive function to count the number of items in a list.
def recursive_count(arr:list):
    if len(arr) == 0:
        return 0
    
    return 1 + recursive_count(arr[1:])
    
    
# 4.3 Find the maximum number in a list.
def max_number(arr:list, current_max = float('-inf')):

    if len(arr) == 0:
        return current_max
    
    max_local_number = arr[0]

    if max_local_number > current_max:
        return max_number(arr[1:], max_local_number)
    else:
        return max_number(arr[1:], current_max)
    
# 4.4 Remember binary search from chapter 1? It’s a divide-and-conquer
# algorithm, too. Can you come up with the base case and recursive
# case for binary search?
def binary_search(arr: list, element):
    if not arr:
        return False

    mid = len(arr) // 2
    if arr[mid] == element:
        return True
    if arr[mid] > element:
        return binary_search(arr[:mid], element)
    return binary_search(arr[mid + 1:], element)


# outra forma de usar binary search sem slicing
def binary_search_rec(arr, x, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1

    if lo > hi:
        return -1

    mid = (lo + hi) // 2
    v = arr[mid]

    if v == x:
        return mid
    if v > x:
        return binary_search_rec(arr, x, lo, mid - 1)
    return binary_search_rec(arr, x, mid + 1, hi)




if __name__ == "__main__":
    # print(recursive_count([1,2,3,4,5]))
    # print(recursive_sum([1,2,3,4,5]))
    # # print(sum([1,2,3,4,5]))  # Output: 15
    # # print(sum([]))           # Output: 0
    # print(max_number([-10, -2, -3]))  # Output: 11
    print(binary_search([1,2,3,4,5],1))