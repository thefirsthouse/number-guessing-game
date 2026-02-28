import random


def core(user_number: int, bot_number: int, attempts: int) -> None:
    """Game manager"""

    if user_number > bot_number:
        print(f"Incorrect! The number is greater than {user_number}.")
    elif user_number < bot_number:
        print(f"Incorrect! The number is less than {user_number}.")
    else:
        print(f"Congratulations! You guessed the correct number in {attempts} attempts.")


def difficulty(difficulty_level: int) -> int:
    """Return the range of attempts depend on difficulty level"""

    match difficulty_level:
        case 1:
            return 10
        case 2:
            return 5
        case 3:
            return 3


def main():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number.")
    print("Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")

    try:
        difficulty_level = int(input("Enter your choice: "))
    except (ValueError, TypeError):
        print("Enter the number of difficulty level from 1 to 3.")
        return -1
    else:
        if difficulty_level == 0 or difficulty_level > 3:
            print("Enter the number of difficulty level from 1 to 3.")
            return -1
        else:
            print("Let's start the game!")
    
    attempts = difficulty(difficulty_level)
    bot_number = random.randint(1, 100)

    guessed = False
    for _ in range(attempts + 1):
        try:
            user_number = int(input("Enter your guess: "))
        except ValueError:
            print("Enter number from 1 to 100!")
        
        if user_number not in range(1, 100 + 1):
            print("Enter number from 1 to 100!")
        elif user_number > bot_number:
            print(f"Incorrect! The number is less than {user_number}.")
        elif user_number < bot_number:
            print(f"Incorrect! The number is greater than {user_number}.")
        else:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            guessed = True
            break
    
    if not guessed:
        print(f"Unfortunately, you've lost. Number was {bot_number}")
    return 0


if __name__ == "__main__":
    main()
