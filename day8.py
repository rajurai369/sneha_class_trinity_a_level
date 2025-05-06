import random

# Display function to print the 2D array
def display_array(array):
    for row in array:
        for val in row:
            print(f"{val:3}", end=" ")
        print()

# Initialize 10x10 array with random integers
def main():
    array = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]
    return array

# Bubble sort for each row in the 2D array
def bubble_sort(array):
    for row in array:
        for i in range(len(row) - 1):
            for j in range(len(row) - i - 1):
                if row[j] > row[j + 1]:
                    row[j], row[j + 1] = row[j + 1], row[j]
    return array

# Recursive Binary Search in the first row (row 0)
def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper >= Lower:
        Mid = (Lower + Upper) // 2
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        elif SearchArray[0][Mid] > SearchValue:
            return BinarySearch(SearchArray, Lower, Mid - 1, SearchValue)
        else:
            return BinarySearch(SearchArray, Mid + 1, Upper, SearchValue)
    return -1  # Not found

# Main execution
array = main()

print("Original 2D Array:")
display_array(array)

# Sort the array row-wise
array = bubble_sort(array)

print("\nSorted 2D Array (Each row sorted in ascending order):")
display_array(array)

# Pick test values for binary search
value_in_array = array[0][5]  # Definitely exists in row 0
value_not_in_array = 999      # Not in the range 1–100

# Perform binary search tests
print(f"\nBinary search for existing value {value_in_array} in first row:")
result1 = BinarySearch(array, 0, 9, value_in_array)
print("Result:", result1 if result1 != -1 else "Not found")

print(f"\nBinary search for non-existing value {value_not_in_array} in first row:")
result2 = BinarySearch(array, 0, 9, value_not_in_array)
print("Result:", result2 if result2 != -1 else "Not found")
