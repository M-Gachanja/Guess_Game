import random

def get_difficulty():
    print("Choose Difficulty Level:")
    print("1. Easy (10 tries)")
    print("2. Medium (7 tries)")
    print("3. Hard (5 tries)")
    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice == '1':
            return 10
        elif choice == '2':
            return 7
        elif choice == '3':
            return 5
        else:
            print("Invalid choice. Try again.")

def get_hint(secret):
    hints = []
    if secret % 2 == 0:
        hints.append("The number is even.")
    else:
        hints.append("The number is odd.")
    if secret % 3 == 0:
        hints.append("The number is divisible by 3.")
    if secret % 5 == 0:
        hints.append("The number is divisible by 5.")
    return random.choice(hints)

def save_high_score(username, attempts_used):
    with open("high_scores.txt", "a") as file:
        file.write(f"{username} - {attempts_used} attempts\n")

def display_leaderboard():
    print("\n🏆 Leaderboard (High Scores):")
    try:
        with open("high_scores.txt", "r") as file:
            scores = file.readlines()
            scores.sort(key=lambda x: int(x.split('-')[1].split()[0]))
            for line in scores[:5]:  # Show top 5
                print(line.strip())
    except FileNotFoundError:
        print("No high scores yet.")

def play_game():
    secret_number = random.randint(1, 100)
    max_attempts = get_difficulty()
    attempts = 0
    wrong_guesses = 0

    print("\nGuess the number between 1 and 100!")

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}. Your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
            username = input("Enter your name for the leaderboard: ")
            save_high_score(username, attempts)
            display_leaderboard()
            return
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        wrong_guesses += 1
        if wrong_guesses == 3:
            print(f"💡 Hint: {get_hint(secret_number)}")

    print(f"\n❌ Game Over! The number was {secret_number}.")
    display_leaderboard()

# Run the game
play_game()
