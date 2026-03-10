import random

def roll_dice(num_dice, num_sides):
    """
    Simulates rolling a specified number of dice with a given number of sides.

    Args:
        num_dice (int): The number of dice to roll.
        num_sides (int): The number of sides on each die (e.g., 6 for a standard die).

    Returns:
        list: A list of integers representing the result of each dice roll.
    """
    results = []
    # Loop for each die the user wants to roll
    for _ in range(num_dice):
        # Generate a random number between 1 and the specified number of sides (inclusive)
        roll = random.randint(1, num_sides)
        results.append(roll)
    return results

def main():
    """
    Main function to handle user input and display results.
    """
    print("Welcome to the Dice Rolling Simulator!")

    while True:
        try:
            # Get the number of dice from the user and validate input
            num_dice_input = input("How many dice do you want to roll? (Enter a number >= 1): ")
            num_dice = int(num_dice_input)
            if num_dice < 1:
                print("Please enter a number greater than or equal to 1.")
                continue

            # Get the number of sides per die from the user and validate input
            num_sides_input = input("How many sides on each die? (Enter a number >= 1): ")
            num_sides = int(num_sides_input)
            if num_sides < 1:
                print("Please enter a number greater than or equal to 1.")
                continue

            # Perform the dice roll simulation
            roll_results = roll_dice(num_dice, num_sides)

            # Display the results
            print(f"\nRolling {num_dice} D{num_sides} dice...")
            print("Results:", roll_results)
            print(f"Total sum: {sum(roll_results)}\n")

            # Ask the user if they want to roll again
            roll_again = input("Roll again? (y/n): ").lower()
            if roll_again != 'y':
                print("Thanks for playing!")
                break

        except ValueError:
            # Handle cases where the user enters non-integer input
            print("Invalid input. Please enter a valid integer number.")
        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    main()
