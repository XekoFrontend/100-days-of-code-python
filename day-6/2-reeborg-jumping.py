# 66. Jumping over Hurdles with Variable Heights
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