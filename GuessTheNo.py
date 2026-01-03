#Welcome to guess the number game
import random

def main():
    print("Welcome to the Guess the Number Game!")
    print(" think a number between 1 To 100.")

    number = random.randint(1, 100) #Random.Randint(a , b) is a function in Python that gives a random whole number (integer) between two numbers.
    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess: "))  # We are taking an input from the user.
            attempts += 1
            if guess < number: #conditional statements.
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")

            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError: # Handle invalid input
            print("Please enter a valid integer.")
main()
        
