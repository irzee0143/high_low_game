import random

# Constants
NUM_ROUNDS = 5  # Number of rounds to play

def high_low_game():
    print("Welcome to the High-Low Game!")
    print("-" * 32)

    score = 0  # Initialize the score

    for round_number in range(1, NUM_ROUNDS + 1):
        print(f"\nRound {round_number}")
        
        # Generate random numbers for player and computer
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        # Display player's number
        print(f"Your number is {player_number}")

        # Get user's guess
        while True:
            user_guess = input("Do you think your number is higher or lower than the computer's? (Type 'higher' or 'lower'): ").strip().lower()
            if user_guess in ("higher", "lower"):
                break
            else:
                print("Invalid input. Please type 'higher' or 'lower'.")

        # Determine if the user's guess is correct
        if (user_guess == "higher" and player_number > computer_number) or (user_guess == "lower" and player_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1  # Increment the score
        elif player_number == computer_number:
            print(f"It's a tie! The computer's number was also {computer_number}. No points this round.")
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        # Display the current score
        print(f"Your score is now {score}")

    # Game over, display final results
    print("\nThanks for playing!")
    print("-" * 32)
    print(f"Your final score is {score}")

    # Conditional ending messages
    if score == NUM_ROUNDS:
        print("Perfect score! You're a High-Low master!")
    elif score > NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time! Keep practicing!")

# Start the game
high_low_game()
