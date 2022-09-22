#include <iostream>
using namespace std;
void merge(int array[], int const left, int const mid,
		int const right)
{
	auto const subArrayOne = mid - left + 1;
	auto const subArrayTwo = right - mid;

	// Create temp arrays
	auto *leftArray = new int[subArrayOne],
		*rightArray = new int[subArrayTwo];

	// Copy data to temp arrays leftArray[] and rightArray[]
	for (auto i = 0; i < subArrayOne; i++)
		leftArray[i] = array[left + i];
	for (auto j = 0; j < subArrayTwo; j++)
		rightArray[j] = array[mid + 1 + j];

	auto indexOfSubArrayOne
		= 0, // Initial index of first sub-array
		indexOfSubArrayTwo
		= 0; // Initial index of second sub-array
	int indexOfMergedArray
		= left; 
	while (indexOfSubArrayOne < subArrayOne
		&& indexOfSubArrayTwo < subArrayTwo) {
		if (leftArray[indexOfSubArrayOne]
			<= rightArray[indexOfSubArrayTwo]) {
			array[indexOfMergedArray]
				= leftArray[indexOfSubArrayOne];
			indexOfSubArrayOne++;
		}
		else {
			array[indexOfMergedArray]
				= rightArray[indexOfSubArrayTwo];
			indexOfSubArrayTwo++;
		}
		indexOfMergedArray++;
	}
	while (indexOfSubArrayOne < subArrayOne) {
		array[indexOfMergedArray]
			= leftArray[indexOfSubArrayOne];
		indexOfSubArrayOne++;
		indexOfMergedArray++;
	}
	while (indexOfSubArrayTwo < subArrayTwo) {
		array[indexOfMergedArray]
			= rightArray[indexOfSubArrayTwo];
		indexOfSubArrayTwo++;
		indexOfMergedArray++;
	}
	delete[] leftArray;
	delete[] rightArray;
}
void mergeSort(int array[], int const begin, int const end)
{
	if (begin >= end)
		return; // Returns recursively

	auto mid = begin + (end - begin) / 2;
	mergeSort(array, begin, mid);
	mergeSort(array, mid + 1, end);
	merge(array, begin, mid, end);
}

void printArray(int A[], int size)
{
	for (auto i = 0; i < size; i++)
		cout << A[i] << " ";
}
int nearest_neighbor(int array[], int n, int val, int index_val, int end, bool side)
{
    int mid = (end-index_val)/2;
    if(side)
    {

    }
}
int find_Range(int array[], int n, int val)
{
    int rval= val+50;
    int lval = val-50;
    
}


// Driver code
int main()
{

    int arr[]= {30, 50, 35, 26, 72, 65, 54, 90, 50, 60, 120, 100, 80};
    int radius = 30;
	auto arr_size = sizeof(arr) / sizeof(arr[0]);

	mergeSort(arr, 0, arr_size - 1);
	cout << "\nSorted array is \n";
	printArray(arr, arr_size);
	return 0;
}


