# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
  
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()  
    move()
    turn_left()

while not at_goal():
    # Angela's solution that uses if/else    
    while front_is_clear() and not at_goal():
        move()  

    while wall_in_front() and not at_goal():
        jump()
