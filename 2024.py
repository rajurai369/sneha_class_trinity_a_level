# -----------------------------
# Question 1(a) – ReadWords()
# -----------------------------
WordArray = []
NumberWords = 0

def ReadWords(filename):
    global WordArray, NumberWords
    WordArray = []  # Reset list before reading
    try:
        with open(filename, 'r') as file:
            lines = file.read().splitlines()
            if lines:
                WordArray.append(lines[0])  # Main word
                for line in lines[1:]:
                    if line.strip():
                        WordArray.append(line.strip())
                NumberWords = len(WordArray) - 1  # Exclude main word
                Play()  # Question 1(d)(i) – Call Play()
            else:
                print("File is empty.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# -----------------------------
# Question 1(c)(ii) – Play()
# -----------------------------
def Play():
    global WordArray, NumberWords
    main_word = WordArray[0]
    print(f"\nMain word: {main_word}")
    print(f"Number of possible answers: {NumberWords}")

    correct_count = 0
    while True:
        user_input = input("Enter a word (or 'no' to stop): ").strip().lower()
        if user_input == 'no':
            break

        if user_input in WordArray[1:]:
            print("Correct!")
            index = WordArray.index(user_input)
            WordArray[index] = ""  # Replace with null/empty string
            correct_count += 1
        else:
            print("Not an answer.")

    print(f"\nYou got {correct_count} correct answers.")
    if NumberWords > 0:
        percentage = (correct_count / NumberWords) * 100
        print(f"Your score: {percentage:.2f}%")

    missed_answers = [word for word in WordArray[1:] if word != ""]
    if missed_answers:
        print("You missed the following answers:")
        for word in missed_answers:
            print(word)
    else:
        print("You found all the answers!")

# -----------------------------
# Question 1(b) – Main Program
# -----------------------------
difficulty = input("Enter difficulty level (easy, medium, hard): ").strip().lower()

filename_map = {
    "easy": "Easy.txt",
    "medium": "Medium.txt",
    "hard": "Hard.txt"
}

if difficulty in filename_map:
    ReadWords(filename_map[difficulty])
else:
    print("Invalid difficulty level.")
