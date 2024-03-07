import random
import game_data
import art
import os

data = game_data.data

def fetch_data():
    """Fetches a random item from the data."""
    return data[random.randint(0, len(data)-1)]

def compare(item1, item2):
    """
    Compares the follower counts of two items.

    Args:
        item1 (dict): The first item.
        item2 (dict): The second item.

    Returns:
        str: 'A' if item1 has more followers, 'B' otherwise.
    """
    num1 = item1['follower_count'] 
    num2 = item2['follower_count']
    if num1 > num2:
        return 'A'
    else:
        return 'B'

new_game = True

# initiates a new game state.
while new_game:
    score = 0
    loop = True
    print(art.logo)
    
    # loops through asking the questions.
    while loop:
        # call the fetch_data function and assign the return value to the items.
        item1 = fetch_data()
        item2 = fetch_data()
        handler = True

        # handles input error.
        while handler:
            print(f"Compare A: {item1['name']}, {item1['description']}, from {item1['country']}.")
            print(art.vs)
            print(f"Against B: {item2['name']}, {item2['description']}, from {item2['country']}.")
            users_input = input("Who has more followers? Type 'A' or 'B': ").upper()
            os.system("cls")

            # game logic.
            if users_input == 'A' or users_input == 'B':
                # compares user input with the return value.
                if users_input == compare(item1, item2):
                    score += 1
                    handler = False
                    print(art.logo)
                    print(f"Your right! Current score: {score}")
                else:
                    loop = False
                    handler = False
                    print(art.logo)
                    print(f"Sorry, that's wrong. Final score: {score}")
            else:
                print("Please Enter 'A' or 'B'.")

    again = input("Do you want to play again,\ninput 'yes' or 'no': ")

    if again == 'yes':
        os.system('cls')
    else:
        new_game = False

input("Tap Enter to Exit!")
