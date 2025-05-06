
DataArray = []

with open("Data.txt", "r") as file:
    for line in file:
        numbers = line.strip().split()
        for num in numbers:
            if len(DataArray) < 25:
                DataArray.append(int(num))
            else:
                break

# ----------- 1(b)(i): Procedure PrintArray() -----------
def PrintArray(arr):
    for item in arr:
        print(item, end=' ')
    print()  # New line at the end

# ----------- 1(c): Function LinearSearch() -----------
def LinearSearch(arr, search_value):
    count = 0
    for item in arr:
        if item == search_value:
            count += 1
    return count

# ----------- 1(b)(ii): Output contents of DataArray -----------
print("Contents of DataArray:")
PrintArray(DataArray)

# ----------- 1(d)(i): User input, validation, search, output -----------
while True:
    try:
        user_input = int(input("Enter a whole number between 0 and 100: "))
        if 0 <= user_input <= 100:
            break
        else:
            print("Invalid input. Please enter a number between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid whole number.")

# Call LinearSearch and display result
occurrences = LinearSearch(DataArray, user_input)
print(f"The number {user_input} is found {occurrences} times.")

# ----------- END OF PROGRAM -----------
