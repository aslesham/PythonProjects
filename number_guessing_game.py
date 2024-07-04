import random

print("Welcme to the Number Guessing Game!!\nI'm thinking of a number between 1 and 100")
number = random.randint(1,100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def guesses(attempts):
    for i in range(attempts):
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high.")
            attempts = attempts - 1
            print(f"You have {attempts} more attempts to guess")
        elif guess < number:
            print("Too low.")
            attempts = attempts - 1
            print(f"You have {attempts} more attempts to guess")
        elif guess == number:
            print(f"You got it! The number was {number}")
    if attempts == 0:
        print(f"You lose! The number was {number}")
        

if difficulty == "easy":
    print("You have 10 attempts to guess the number!")
    attempts = 10
    guesses(attempts)

if difficulty == "hard":
    print("You have 5 attempts to guess the number!")
    attempts = 5
    guesses(attempts)








