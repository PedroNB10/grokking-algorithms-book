def quicksort(array):
    if len(array) < 2:
        return array # Base case: arrays with 0 or 1 element are already “sorted.”
    else:
        pivot = array[0] # recursive case
        less = [i for i in array[1:] if i <= pivot] # Sub-array of all the elements less than the pivot
        greater = [i for i in array[1:] if i > pivot] # Sub-array of all the elements greater than the pivot
        return quicksort(less) + [pivot] + quicksort(greater)
    
import random

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot_index = random.randint(0, len(array) - 1)
        pivot = array[pivot_index]

        # Exclude the pivot from the subarrays
        less = [i for j, i in enumerate(array) if i <= pivot and j != pivot_index]
        greater = [i for j, i in enumerate(array) if i > pivot and j != pivot_index]

        return quicksort(less) + [pivot] + quicksort(greater)

    
if __name__ == "__main__":
    pass