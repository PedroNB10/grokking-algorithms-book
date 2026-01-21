def findSmallest(arr): 
    smallest = arr[0]
    smallest_index = 0
    # from the second element to the end
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        newArr.append(arr.pop(smallest_index)) # remove the smallest element in index smallest_index and append it to newArr
    return newArr


if __name__ == "__main__":
    sample_array = [64, 25, 12, 22, 11]
    sorted_array = selectionSort(sample_array)
    print("Sorted array:", sorted_array)