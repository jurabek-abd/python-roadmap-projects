from random import randint

print("\nWelcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 5 chances to guess the correct number.")

print("\nPlease select the difficulty level:")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)")

is_level_chosen = False
# is_game_running = False
guessing_number = 0
attempts = 0

while not is_level_chosen:
    user_level_choice = int(input("\nEnter your choice: "))

    if user_level_choice == 1:
        attempts = 10
        print("Great! You have selected the Easy difficulty level.")
    elif user_level_choice == 2:
        attempts = 5
        print("Great! You have selected the Medium difficulty level.")
    elif user_level_choice == 3:
        attempts = 3
        print("Great! You have selected the Hard difficulty level.")
    else:
        print("Invalid level. Please select the correct level.")
        continue

    print("Let's start the game!")
    is_level_chosen = True
    # is_game_running = True
    guessing_number = randint(1, 101)

guesses = 0
while guesses < attempts:
    try:
        user_guess = int(input("\nEnter your guess: "))

        if user_guess < 1 or user_guess > 100:
            print("Please keep it between 1 and 100")
            continue

        guesses += 1

        if user_guess < guessing_number:
            print(f"Incorrect! The number is greater than {user_guess}.")
        elif user_guess > guessing_number:
            print(f"Incorrect! The number is less than {user_guess}.")
        elif user_guess == guessing_number:
            print(
                f"Congratulations! You guessed the correct number in {guesses} attempts."
            )
            break
    except ValueError as e:
        print(f"Error: {e}")
else:
    print(f"\nYou failed. It was {guessing_number}")
