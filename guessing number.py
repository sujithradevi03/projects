import random

# Generate a random number between 1 and 100 (you can adjust the range as needed)
secret_number = random.randint(1, 5)

attempts = 0

while True:
    guess = input("Guess the number (between 1 and 5): ")
    
    try:
        guess = int(guess)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    attempts += 1
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts.")
        break

