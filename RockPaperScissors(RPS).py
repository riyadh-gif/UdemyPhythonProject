import random
# Rock Paper Scissors ASCII Art

# Rock
Rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
Rock
"""

# Paper
Paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

Paper
"""

# Scissors
Scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

Scissors
"""

user = int(input("what do you chose? type 0 for rock, 1 for paper, or 2 for Scissors: "))
image = [Rock,Paper,Scissors]
computer_choice = random.choice(image)
computer_choice_index = image.index(computer_choice)

#tunjukan hasil
print("Your Choice: ")
print(image[user])
print("Computer Choice: ")
print(computer_choice)

#penentuan hasil
if user == computer_choice_index:
 print("Your Draw")

elif (user == 0 and computer_choice_index == 1) or (user == 1 and computer_choice_index == 2) or (user == 2 and computer_choice_index == 0):
 print("you lose")

else:
 print("you win")
 





    

 
    
    

 
 



