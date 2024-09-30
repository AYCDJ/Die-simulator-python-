import random

def roll_dice(num_dice=1, num_sides=6):
    try:
        # Check if die can be real
        if num_dice < 1 or num_sides < 2:
            raise ValueError("Number of dice must be at least 1, and dice must have at least 2 sides.")

        # Roll the die
        rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
        return rolls
    except TypeError:
        return "Invalid input: Please enter integers for both the number of dice and sides."
    except ValueError as e:
        return str(e)

def main():
    while True:
        # Ask for input
        num_dice = int(input("Enter the number of dice: "))
        num_sides = int(input("Enter the number of sides per die: "))
        
        # Roll the die and show the result
        result = roll_dice(num_dice, num_sides)

        if isinstance(result, list):
            print(f"Rolls: {result}")
        else:
            print(result)  # Print any error messages

        # Ask if the user wants to roll again
        again = input("Do you want to roll again? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("later sk8r")
            break

# Start the simulator
if __name__ == "__main__":
    main()
