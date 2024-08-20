rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
import random
user_choice = int(input())
computer_choice = random.randint(0,2)
if user_choice == 0:
    if computer_choice ==0:
        print(rock)
        print("Computer chose:")
        print(rock)
        print("It's a draw")
    if computer_choice ==1:
        print(rock)
        print("Computer chose:")
        print(paper)
        print("You lose")
    if computer_choice ==2:
        print(rock)
        print("Computer chose:")
        print(scissors)
        print("You win")
if user_choice ==1:
    if computer_choice ==0:
        print(paper)
        print("Computer chose:")
        print(rock)
        print("You win")
    if computer_choice ==1:
        print(paper)
        print("Computer chose:")
        print(paper)
        print("It's a draw")
    if computer_choice ==2:
        print(paper)
        print("Computer chose:")
        print(scissors)
        print("You lose")
if user_choice ==2:
    if computer_choice ==0:
        print(scissors)
        print("Computer chose:")
        print(rock)
        print("You lose")
    if computer_choice ==1:
        print(scissors)
        print("Computer chose:")
        print(paper)
        print("You win")
    if computer_choice ==2:
        print(scissors)
        print("Computer chose:")
        print(scissors)
        print("It's a draw")
