import random

def guess_the_number_game():
    """
    A number guessing game with a limited number of attempts.
    """
    # 1. Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    max_attempts = 5
    attempts_left = max_attempts
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print(f"I have selected a number between 1 and 100. You have {max_attempts} attempts.")

    # 2. Use a while loop to repeatedly ask the user for guesses
    while attempts_left > 0 and not guessed_correctly:
        try:
            user_guess = int(input(f"Enter your guess (Attempts left: {attempts_left}): "))
        except ValueError:
            print("Invalid input. Please enter a valid integer number.")
            continue # Skip the rest of the loop and ask for input again

        # 3. Provide feedback to the user
        if user_guess == secret_number:
            print(f"Congratulations! You've guessed the number {secret_number} correctly!")
            guessed_correctly = True
        elif user_guess < secret_number:
            print("Too low! Try a higher number.")
            attempts_left -= 1
        else:
            print("Too high! Try a lower number.")
            attempts_left -= 1

    # Check if the game ended because of running out of attempts
    if not guessed_correctly:
        print(f"Sorry, you ran out of attempts! The correct number was {secret_number}.")

if __name__ == "__main__":
    guess_the_number_game()
