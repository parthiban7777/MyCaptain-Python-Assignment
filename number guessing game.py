import random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            print("It took you", attempts, "attempts.")
            break
        elif user_guess < secret_number:
            print("Too low. Try again!")
        else:
            print("Too high. Try again!")

guess_number()
