

player_names = [""] * 11  # 10 from file + 1 new
player_scores = [0] * 11

# ---------- 1(b) ReadHighScores() ----------
def ReadHighScores():
    try:
        with open("HighScore.txt", "r") as file:
            for i in range(10):
                line = file.readline().strip()
                if not line:
                    break
                name, score = line.split()
                player_names[i] = name
                player_scores[i] = int(score)
    except FileNotFoundError:
        print("HighScore.txt not found. Starting with empty list.")

# ---------- 1(c) OutputHighScores() ----------
def OutputHighScores():
    for i in range(10):
        if player_names[i] != "":
            print(f"{player_names[i]} {player_scores[i]:,}")

# ---------- 1(e)(ii) InsertNewHighScore(name, score) ----------
def InsertNewHighScore(name, score):
    player_names[10] = name
    player_scores[10] = score
    combined = list(zip(player_names, player_scores))
    combined.sort(key=lambda x: x[1], reverse=True)
    for i in range(10):
        player_names[i], player_scores[i] = combined[i]

# ---------- 1(f) WriteTopTen() ----------
def WriteTopTen():
    with open("NewHighScore.txt", "w") as file:
        for i in range(10):
            if player_names[i] != "":
                file.write(f"{player_names[i]} {player_scores[i]}\n")

# ---------- 1(d) & 1(e)(iii) Main Program ----------
if __name__ == "__main__":
    ReadHighScores()

    print("\nOriginal High Scores:")
    OutputHighScores()

    # 1(e)(i) Input new name and score
    while True:
        new_name = input("\nEnter new player name (3 characters): ").strip().upper()
        if len(new_name) == 3:
            break
        print("Name must be exactly 3 characters.")

    while True:
        try:
            new_score = int(input("Enter score (1 to 100000): "))
            if 1 <= new_score <= 100000:
                break
            else:
                print("Score must be between 1 and 100000.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Insert into top 10 if appropriate
    InsertNewHighScore(new_name, new_score)

    print("\nUpdated High Scores:")
    OutputHighScores()

    # Save to file
    WriteTopTen()
    print("\nNew top 10 saved to NewHighScore.txt")
