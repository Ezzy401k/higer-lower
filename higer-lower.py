import random
import game_data
data = game_data.data
import os

def fetch_data():
    item = {}
    item = data[random.randint(0,len(data)-1)]
    return item

score = 0
loop = True
while loop:

    item1 = fetch_data()
    item2 = fetch_data()

    def compare(item1, item2):
        num1 = item1['follower_count'] 
        num2 = item2['follower_count']
        if num1 > num2:
            return 'A'
        else:
            return 'B'

    print(f"Compare A: {item1['name']}, {item1['description']}, from {item1["country"]}.")
    print(f"Against B: {item2['name']}, {item2['description']}, from {item2["country"]}.")

    users_input = input("Who has more followers? Type 'A' or 'B': ")
    os.system("cls")

    if users_input == compare(item1, item2):
        score += 1
        print(f"Your rigth! Current score: {score}")
    else:
        loop = False
        print(f"Sorry, that's wrong. Final score: {score}")


