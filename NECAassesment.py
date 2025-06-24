print("Welcome to my rock paper scissor game!")
score = 0


import random
user = input("Choose one! rock paper scissor!")
computer = random.choice(["rock", "paper", "scissor"])
print ("You chose: " + user)
print ("Computer chose: " + computer)


if user == computer:
    print("Tie")
    score += 0
if user == "rock" and computer == "paper" or user == "paper" and computer == "scissor" or user == "scissor" and computer == "rock":
    print("Lose")
    score -= 1
if user == "scissor" and computer == "paper" or user == "paper" and computer =="rock" or user == "rock" and computer == "scisssor":
    print("Win")
    score += 1