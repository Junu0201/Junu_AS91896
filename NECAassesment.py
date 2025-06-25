print("Welcome to my rock paper scissor game!")
yes = 0
while yes < 1:
    start = input("Are you ready to play?")
    score = 0
    if start =="yes":
        print ("Nice let's start it")
        yes += 1
    elif start == "no":
        print ("Okay")
        yes = 0
    else:
        print ("?")
        yes = 0

loop = 0
while loop < 5:
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
    loop += 1
print ("Your score is {}".format (score))
