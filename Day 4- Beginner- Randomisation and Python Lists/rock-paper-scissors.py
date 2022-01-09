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

#Write your code below this line 👇

def print_art(response):
  if response == 0:
    print(rock)
  elif response == 1:
    print(paper)
  else:
    print(scissors)

response = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if not response.isdecimal() or (int(response) < 0 or int(response) > 2):
  print("You typed wrong number. You lose!")
else:
  response = int(response)
  computer = random.randint(0, 2)
  print("You chose:")
  print_art(response)

  print("Computer chose:")
  print_art(computer)

  if response == computer:
    print("It's a draw!")
  elif (response == 1 and computer == 0) or (response == 2 and computer == 1) or (response == 0 and computer == 2):
    print("You win!")
  else:
    print("You lose!")



