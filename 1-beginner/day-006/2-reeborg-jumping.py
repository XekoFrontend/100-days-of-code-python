# Jumping over Hurdles with Variable Heights
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    while wall_in_front():
        turn_left()
    while wall_on_right() and front_is_clear() and not at_goal():
        move()
    while right_is_clear():
        turn_right()
        move()
        turn_right()
        move()

while not at_goal():    
    if wall_in_front():
        jump()
    else:
        move()


###### --- Angela’s solution for the 'jump' function
'''
def jump():
    turn_left()    
    while wall_on_right():
        move()    
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
'''


##### --- Another one of my solutions using a while loop :D
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_right()
    move()
    turn_right()
    move()    
    
while not at_goal():
    while wall_in_front() and not at_goal():
        turn_left()
    while front_is_clear() and wall_on_right() and not at_goal():
        move()
    while right_is_clear() and not at_goal():
        jump()
'''