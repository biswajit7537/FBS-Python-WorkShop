import random


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

game_objects = [rock,paper,scissors]
print("______ Welcome To Rock Paper Scissors Game______\n\n")

user_choice = int(input("Enter your choice : ( Write 0 for Rock, 1 for Paper, 2 for Scissors )\n"))
print("User Choice : ")
print(game_objects[user_choice])

computer_choice = random.randint(0,2)
print("Computer Choice : ")
print(game_objects[computer_choice])

if user_choice >= 3 or user_choice < 0 :
    print("Invalid Choice !!")
elif user_choice == computer_choice:
    print("Match Draw !!")
elif user_choice == 0 and computer_choice == 2:
    print("You Win !")
elif computer_choice == 0 and user_choice == 2:
    print("You Lose !")
elif computer_choice > user_choice:
    print("You Lose !")
elif user_choice > computer_choice:
    print("You Win !") 





