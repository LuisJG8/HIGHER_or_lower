from art import logo, vs
from data_game import data
import random

celeb_A = random.choice(data)
celeb_B = random.choice(data)
if celeb_A == celeb_B:
    celeb_B = random.choice(data)
POINTS = 0
flag = True

while flag:
    celeb_C = random.choice(data)
    print(logo)
    print(f"\nCompare A: {celeb_A["name"]}, a {celeb_A["description"]}, from {celeb_A["country"]}")
    print(vs)
    print(f"Compare B: {celeb_B["name"]}, a {celeb_B["description"]}, from {celeb_B["country"]}")

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    if answer == 'a' and celeb_A["follower_count"] > celeb_B["follower_count"]:
        POINTS += 1
        celeb_A = celeb_A #easier to visualize
        celeb_B = celeb_C
    elif answer == 'a' and celeb_A["follower_count"] < celeb_B["follower_count"]:
        print(f"Incorrect, final score {POINTS}")
        break

    if answer == 'b' and celeb_B["follower_count"] > celeb_A["follower_count"]:
        POINTS += 1
        celeb_A = celeb_B
        celeb_B = celeb_C
    elif answer == 'b' and celeb_B["follower_count"] < celeb_A["follower_count"]:
        print(f"Incorrect, final score {POINTS}")
        break