import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100
    
    # Generate a random number between lower_bound and upper_bound
    number_to_guess = random.randint(lower_bound, upper_bound)
    
    attempts = 0
    guessed_correctly = False
    
    print(f"I have selected a number between {lower_bound} and {upper_bound}. Can you guess what it is?")
    
    while not guessed_correctly:
        try:
            # Get user's guess
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check if the guess is too low, too high, or correct
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
        
        except ValueError:
            # Handle invalid input
            print("Invalid input. Please enter a number.")
    
if __name__ == "__main__":
    number_guessing_game()
