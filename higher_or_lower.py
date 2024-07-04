import random
from higherorlower_data import data


def get_account():
  return random.choice(data)


def format_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"


def comparison(account_a, account_b):
  a_followers = account_a["follower_count"]
  b_followers = account_b["follower_count"]
  if a_followers > b_followers:
    return "a"
  else:
    return "b"


continue_game = True
score = 0
print("Welcome to the Higher Lower Game!")
account_a = get_account()
account_b = get_account()

while continue_game:
  print("Compare A: " + format_data(account_a))
  print("Against B: " + format_data(account_b))
  answer = input("Who has more followers? Type 'A' or 'B': ").lower()
  if answer == comparison(account_a, account_b):
    score = score + 1
    print(f"You're right! Your score is {score}")
    account_a = account_b
    account_b = random.choice(data)
    continue_game = True
  else:
    print(f"Sorry, that's wrong. Your final score is {score}")
    option = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if option == 'n':
      continue_game = False
