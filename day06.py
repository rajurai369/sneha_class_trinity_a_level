
arrayData = []
def linearSearch(target):
    for value in arrayData:
        if value == target:
            return True
    return False


def main():# Main program
    global arrayData
    arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]  
    try:
        user_input = int(input("Enter an integer to search for: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    
    found = linearSearch(user_input)

    if found:
        print(f"The value {user_input} was found in the array.")
    else:
        print(f"The value {user_input} was NOT found in the array.")


main()


def bubbleSort():
    temp = 0
    n = len(arrayData)  
    
  
    for x in range(n-1):  
       
        for y in range(n-1-x):  
           
            if arrayData[y] < arrayData[y + 1]:
                temp = arrayData[y]  
                arrayData[y] = arrayData[y + 1]  
                arrayData[y + 1] = temp  


arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]
print("Original array:", arrayData)

bubbleSort()


print("Sorted array in descending order:", arrayData)

