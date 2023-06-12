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

lst = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for rock, 1 for paper, and 2 for scissors. "))
print("You chose:\n")
print(lst[choice])

comp_choice = random.randint(0,2)
print("Computer chose:\n")
print(lst[comp_choice])

if choice==0 and comp_choice==2:
    print("You Win!")
elif choice==2 and comp_choice==1:
    print("You Win!")
elif choice==1 and comp_choice==0:
    print("You Win!")
else:
    print("You Lose:(")

