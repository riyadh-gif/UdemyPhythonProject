def turn_right():
    turn_left()
    turn_left()
    turn_left()
       
    
def receipe():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
def obstacle():
    turn_left()
    while wall_on_right():  
        move()
    turn_left()
    turn_left()
    turn_left()    
    move()
    turn_left()
    turn_left()
    turn_left()  
    while front_is_clear():  
        move()
    turn_left()
    
while not at_goal():  
    if wall_in_front():  
        obstacle()
    else:
        move()
    
    
    
 

        
    
     
        
