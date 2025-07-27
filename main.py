# Display art
from game_data import data, logo1, vs
# from replit import clear
import random

def format_data(account):
    """Takes the account data and returns the printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

# - Use if statement to check if user is correct
def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess, and the follower counts and returns if they got it right."""
    # This is a long way of doing it
    # if a_followers > b_followers and user_guess == 'a':
    #     return True
    # elif a_followers > b_followers and user_guess == 'b':
    #     return False
    # elif b_followers > a_followers and user_guess == 'b':
    #     return True
    # elif b_followers > a_followers and user_guess == 'a':
    #     return False
    # else:
    #     return None

    if a_followers > b_followers:
        # if user_guess == a:
        #     return True
        # else:
        #     return False
        return user_guess == "a"
    else:
        # if user_guess == b:
        #     return True
        # else:
        #     return False
        return user_guess == "b"

print(logo1)
score = 0
game_should_continue = True
account_b = random.choice(data)

# Make the game repeatable.
while game_should_continue:
    # Generate a random account from the game data

    # Making account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {format_data(account_a)}.")
    print(vs)
    print(f"Against B : {format_data(account_b)}.")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen
    print("\n" * 25) # or we can use clear()
    print(logo1)

    # Check if the user is correct.
    # - Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess.
    # Score keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}.\n")
    else:
        print(f"\nSorry, that's wrong. Final score: {score}.\n")
        game_should_continue = False