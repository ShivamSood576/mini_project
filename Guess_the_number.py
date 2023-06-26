import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Function to play the game
def play_game():
    attempts = 0
    while True:
        # Get user's guess
        guess = int(input("Guess the number (between 1 and 100) \n: "))
        attempts += 1

        # Compare the guess with the secret number
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number correctly!")
            print("Number of attempts:", attempts)
            break

# Start the game
print("Welcome to Guess the Number!")
play_game()
