import random


secret_number = random.randint(1, 100)


max_attempts = 8
attempts = 0

print("Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts.")


while attempts < max_attempts:
    try:
        guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
    except ValueError:
        print("Invalid input!!!!!!!!!!!! Please enter an integer.")


    attempts += 1

    if guess == secret_number:
        print(f" Congratulations!!!!!!!!!!1 You guessed the number in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low!!!!!!!!!!!!!!!!!! Try again, do not give up.")
    else:
        print("Too high!!!!!!!!!!!!!!!!!!! Try again, do not give up.")

if attempts == max_attempts and guess != secret_number:
    print(f"Sorry, you've used all {max_attempts} attempts. The number was {secret_number}, try againnnnnnnnnnnnnnnn.")
