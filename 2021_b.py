
arrayData = []

# ========= PART 2(b)(i) =========
# Function to perform a linear search
def linearSearch(value):
    global arrayData
    for item in arrayData:
        if item == value:
            return True
    return False

# ========= PART 2(c) =========
# Procedure to sort arrayData in descending order using bubble sort
def bubbleSort():
    global arrayData
    temp = 0
    for x in range(len(arrayData) - 1):
        for y in range(len(arrayData) - 1 - x):
            if arrayData[y] < arrayData[y + 1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y + 1]
                arrayData[y + 1] = temp

# ========= PART 2(b)(ii) =========
# Main program
def main():
    global arrayData

    # Initialize array with given data
    arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

    print ("Original array data:")
    print (arrayData)

    # Sort the array in descending order
    bubbleSort()
    print ("Array after bubble sort (descending):")
    print (arrayData)

    # Get user input
    searchValue = int(input("Enter a number to search in the array: "))

    # Search using linearSearch
    found = linearSearch(searchValue)

    # Output result
    if found:
        print ("The number %d was found in the array." % searchValue)
    else:
        print ( "The number %d was NOT found in the array." % searchValue)

# Call the main function
main()
