import random

def number_guessing_game():
    
    
    print("guess the number from 1 to 100")

    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("Too Low! Try again.")
        elif guess > number_to_guess:
            print("Too High! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
number_guessing_game()