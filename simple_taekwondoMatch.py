print('''
,.
  \-'__
 / o.__o____
 \/_/ /.___/--,
   ||\' mrf
   | /
   \_\
   -''
-----------------------------------
''')
print("Hello Champion, welcome to taekwondo tournament")
print("Your Mission For Defeat your enemy at the front you")
print("Match Start Now !!!")
kick = input("What your act (dwi chagi, dolyo chagi, another): ")
point = 0
enemy_point = 0

if kick == "dolyo chagi":
 impact = input("what you havekick: ")
 if impact == "body":
    point += 2
    print("you got 2 point")
  
 elif impact == "head":
    point = point + 3
    print("you got 3 point")

elif kick == "dwi chagi":
 impact = input("what you havekick: ")
 if impact == "body":
    point += 2
    print("you got 3 point")
  
 elif impact == "head":
    point = point + 3
    print("you got 4 point")

elif kick == "dwi hurigi":
 impact = input("what you havekick: ")
 if impact == "body":
    point += 2
    print("you got 3 point")
  
 elif impact == "head":
    point = point + 3
    print("you got 4 point")

else :
  point -= 2
  enemy_point += 2
  print("you have to kick by yout enemy at body")
  
print("YOUR ENEMY want to kick your head !!!")
move = input("What your act (twio chagi, dwichagi, dolyo chagi):  ")

if move == "twio chagi":
 impact = input("What body you hit: ")
 if impact == "body":
  point += 3
  print("gotcha, you have get 3 point")
 
 elif impact == "head":
  point += 4
  print("gotcha, you have get 4 point")
 
 else:
  enemy_point += 1
  print("You get punnishment")

if move == "dwi chagi":
 impact = input("What body you hit: ")
 if impact == "body":
  point += 3
  print("gotcha, you have get 3 point")
 
 elif impact == "head":
  point += 4
  print("gotcha, you have get 4 point")
 
 else:
  enemy_point += 1
  print("You get punnishment")

else:
 enemy_point += 3
 print("You have hit")
 poin -= 1
 print("You fall at arena")
 enemy_point += 1
 point -= 1

print ("===========")
move = input("what your next move: ")

if move == "dolke chagi" or move == "dwi hurigi":
 impact = input("what body your hit: ")
 if move == "head":
  point += 4
  print("your get point")
 
 elif move == "body":
  point += 3
  print("your get point")

else :
 enemy_point += 4
 print("You have hit by your enemy with dolke chagi at head")

print("Match END")
print(f"your point is: {point}")
print(f"enemy poin is : {enemy_point}")

if point > enemy_point:
 print("you win")

elif point == enemy_point :
 print("draw")

else:
 print("You Lose")
 





 
 
 
 
 
 
 
    


    
  
 
    

