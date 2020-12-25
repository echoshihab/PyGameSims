'''My Solution to Day 14 - Higher Lower Game Project from 100 days of Code by Dr. Angela Yu'''

from art import logo, vs
from game_data import data
import random
import os

# print logo
print(logo)


# initiate
choices = []
score = 0

# chose random item fro m data


def initiate_choices(choice_array, data_list):
    if len(choice_array) == 0:
        choices.append(data.pop(random.randint(0, len(data)-1)))
        choices.append(data.pop(random.randint(0, len(data)-1)))
    else:
        choices.pop(0)
        choices.append(data.pop(random.randint(0, len(data)-1)))


def compare_choices(choice_array):
    print(
        f"Compare A: {choice_array[0]['name']}, a {choice_array[0]['description']}, from {choice_array[0]['country']}.")
    print(vs)
    print(
        f"Compare B: {choice_array[1]['name']}, a {choice_array[1]['description']}, from {choice_array[1]['country']}.")


def evaluate_result(user_choice, choice_array):
    if user_choice == 'a':
        return choices[0]['follower_count'] > choices[1]['follower_count']
    elif user_choice == 'b':
        return choices[1]['follower_count'] > choices[0]['follower_count']
    else:
        return False


initiate_choices(choices, data)
compare_choices(choices)

user_input = input("Who has more followers? Type 'A' or 'B' ").lower()

while evaluate_result(user_input, choices):
    score += 1
    os.system('cls')
    print(logo)
    print(f"You are right, Current score is {score}")
    initiate_choices(choices, data)
    compare_choices(choices)
    user_input = input("Who has more followers? Type 'A' or 'B' ").lower()

os.system('cls')
print(logo)
print(f"Sorry that is incorrect, final score is {score}")
