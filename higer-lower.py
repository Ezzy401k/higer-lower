import random
import game_data
data = game_data.data
import os

def fetch_data():
    item = {}
    item = data[random.randint(0,len(data)-1)]
    return item

def compare(item1, item2):
        num1 = item1['follower_count'] 
        num2 = item2['follower_count']
        if num1 > num2:
            return 'A'
        else:
            return 'B'
        

new_game =True

while new_game:
    score = 0
    loop = True
    while loop:

        item1 = fetch_data()
        item2 = fetch_data()

        handler = True
        while handler:

            print(f"Compare A: {item1['name']}, {item1['description']}, from {item1["country"]}.")
            print(f"Against B: {item2['name']}, {item2['description']}, from {item2["country"]}.")
            users_input = input("Who has more followers? Type 'A' or 'B': ").upper()
            os.system("cls")
            if users_input == 'A' or users_input == 'B':
                
                if users_input == compare(item1, item2):
                    score += 1
                    handler = False
                    print(f"Your rigth! Current score: {score}")
                else:
                    loop = False
                    handler = False
                    print(f"Sorry, that's wrong. Final score: {score}")
            else:
                print("Please Enter 'A' or 'B'.")
    again = input("Do you want to play again,\ninput 'yes' or 'no': ")

    if again == 'yes':
        os.system('cls')
    else:
        new_game = False
input("Tap Enter to Exit!")


