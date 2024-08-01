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

#paper(1) beats rock(0)
#scissors(2) beats paper(1)
#rock(0) beats scissors(2)

print("Welcome to Rock Paper Scissors Game!!!")

game_list = [rock, paper, scissors]

choice = int(input("press 0 to chose rock, 1 to chose paper, 2 to chose scissors: "))
print("user choice")
print(game_list[choice])
computer_choice = random.randint(0, 2)
print("computer choice")
print(game_list[computer_choice])
print(f"computer choose {computer_choice}")
if computer_choice == 2 and choice == 0:
    print("you win")
elif computer_choice == 0 and choice == 2:
    print("you lose")
elif computer_choice == 1 and choice == 2:
    print("you win")
elif computer_choice == 0 and choice == 1:
    print("you win")
elif computer_choice > choice:
    print("computer wins")
elif computer_choice == choice:
    print("Draw")
else:
    print("you typed an invalid number you lose")