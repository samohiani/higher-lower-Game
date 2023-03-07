from art import logo 
from art import vs
from game_data import data
from replit import clear
import random
print(logo)

def pick_person():
  return random.choice(data)

def check_answer(score, user_answer, random_dictA, random_dictB):
  game_end = False
  while not game_end:
    if (random_dictA["follower_count"] > random_dictB["follower_count"] and user_answer == "A") or (random_dictA["follower_count"] < random_dictB["follower_count"] and user_answer == "B"):
      score += 1
      clear()
      print(logo)
      print(f"You're right! Current Score = {score}")
      random_dictD = random_dictB
      random_dictC = pick_person()
      print(f"Compare A: {random_dictD['name']}, a {random_dictD['description']}, from {random_dictD['country']}")
      print(vs)
      print(f"Against B: {random_dictC['name']}, a {random_dictC['description']}, from {random_dictC['country']}")
      user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    else:
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")
      game_end = True
    
score = 0
random_dictA = pick_person()
random_dictB = pick_person()
print(f"Compare A: {random_dictA['name']}, a {random_dictA['description']}, from {random_dictA['country']}")
print(vs)
print(f"Against B: {random_dictB['name']}, a {random_dictB['description']}, from {random_dictB['country']}")
user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()

check_answer(score, user_answer, random_dictA, random_dictB)