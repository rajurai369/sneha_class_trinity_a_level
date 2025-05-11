


DataStored = [0] * 20  # Global array with space for up to 20 integers
NumberItems = 0        # Global variable to store number of items

# Part (b): Initialise procedure
def Initialise():
    global DataStored
    global NumberItems

    while True:
        try:
            NumberItems = int(input("Enter the number of integers to input (1–20): "))
            if 1 <= NumberItems <= 20:
                break
            else:
                print("Please enter a number between 1 and 20.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    for i in range(NumberItems):
        while True:
            try:
                number = int(input(f"Enter integer #{i+1}: "))
                DataStored[i] = number
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

# Part (d)(i): BubbleSort procedure
def BubbleSort():
    global DataStored, NumberItems
    for i in range(NumberItems - 1):
        for j in range(NumberItems - 1 - i):
            if DataStored[j] > DataStored[j + 1]:
                DataStored[j], DataStored[j + 1] = DataStored[j + 1], DataStored[j]

# Part (e)(i): BinarySearch function
def BinarySearch(DataToFind):
    global DataStored, NumberItems
    low = 0
    high = NumberItems - 1

    while low <= high:
        mid = (low + high) // 2
        if DataStored[mid] == DataToFind:
            return mid
        elif DataStored[mid] < DataToFind:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Not found

# ================================
# Part (c)(i), (d)(ii), (e)(ii): Main Program
# ================================
NumberItems = 0
Initialise()

print("\nDataStored contents before sorting:")
for i in range(NumberItems):
    print(DataStored[i])

BubbleSort()

print("\nDataStored contents after sorting:")
for i in range(NumberItems):
    print(DataStored[i])

# Search a number
try:
    data_to_find = int(input("\nEnter a number to search for: "))
    index_found = BinarySearch(data_to_find)
    if index_found != -1:
        print(f"Number {data_to_find} found at index {index_found}.")
    else:
        print(f"Number {data_to_find} not found in the array.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
