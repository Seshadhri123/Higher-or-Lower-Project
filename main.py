import art
import game_data
import random


def random_integer():
    R1 = random.randint(0, 49)
    return R1

game_over = False

update_value = random_integer()
index_value = random_integer()

while update_value == index_value:
    index_value = random_integer()

def compare():
        print(art.logo)
        print("Compare A:",game_data.data[update_value]["name"] ,", a",game_data.data[update_value]["description"],", from" ,game_data.data[update_value]["country"])
        print(art.vs)
        print("Compare B:", game_data.data[index_value]["name"], ", a", game_data.data[index_value]["description"],
            ", from", game_data.data[index_value]["country"])
        return index_value


score = 0
index1_value = compare()
while not game_over:
    decision = input("Who has more followers? Type 'A' or 'B':").upper()
    if decision == "A":
        if game_data.data[update_value]["follower_count"] > game_data.data[index1_value]["follower_count"]:
            score += 1
            print("\n"*100)
            print("Correct Answer!,Your score is",score,"onto the next one.")
            index_value = random_integer()
            while update_value == index_value:
                index_value = random_integer()
            index1_value = compare()

        else:
            print("\n" *100)
            print(art.logo)
            print("You lost the game and your score =", score)
            game_over = True
    if decision == "B":
        if game_data.data[update_value]["follower_count"] < game_data.data[index1_value]["follower_count"]:
            score += 1
            print("\n" * 100)
            print("Correct Answer!,Your score is",score," onto the next one.")
            update_value = index1_value
            index_value = random_integer()
            while update_value == index_value:
                index_value = random_integer()
            index1_value = compare()


        else:
            print("\n" *100)
            print(art.logo)
            print("You lost the game and your score =", score)
            game_over = True
