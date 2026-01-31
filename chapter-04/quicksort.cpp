#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

using namespace std;

// Randomized QuickSort function
vector<int> quicksort(const vector<int>& array) {
    if (array.size() < 2) {
        return array; // Base case
    }

    // Random pivot selection
    int pivotIndex = rand() % array.size();
    int pivot = array[pivotIndex];

    vector<int> less, greater;

    for (int i = 0; i < array.size(); ++i) {
        if (i == pivotIndex) continue; // Skip the pivot itself
        if (array[i] <= pivot) {
            less.push_back(array[i]);
        } else {
            greater.push_back(array[i]);
        }
    }

    // Recursive calls
    vector<int> sortedLess = quicksort(less);
    vector<int> sortedGreater = quicksort(greater);

    // Combine results: sortedLess + pivot + sortedGreater
    //sortedLess.insert(...)	We're inserting into sortedLess
    // sortedLess.end()	Insert at the end of sortedLess
    // sortedGreater.begin()	Start copying from the beginning of sortedGreater
    // sortedGreater.end()	Stop copying at the end of sortedGreater (exclusive)

    // sortedLess + pivot + sortedGreater
    sortedLess.push_back(pivot);
    sortedLess.insert(sortedLess.end(), sortedGreater.begin(), sortedGreater.end());

    return sortedLess;
}

// Helper function to print vector
void printArray(const vector<int>& arr) {
    for (int num : arr)
        cout << num << " ";
    cout << endl;
}

int main() {
    srand(time(0)); // Seed the random number generator

    vector<int> arr = {10, 5, 2, 3, 7, 6, 4};
    vector<int> sorted = quicksort(arr);

    cout << "Sorted array: ";
    printArray(sorted);

    return 0;
}
