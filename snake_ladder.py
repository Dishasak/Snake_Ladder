#usedcase3 
def moving(value, position, dice_roll):
    match value:
        case 1: 
            return position, "NoPlay"
        case 2:  
            position += dice_roll
            return position, "Ladder"
        case 3: 
            position -= dice_roll
            return position, "Snake"
        case _:
            return position, "Invalid move"

while position < target:
    dice_roll = random.randint(1, 6)  
    count += 1
   
    event = random.randint(1, 3)
    position, event_name = moving(event, position, dice_roll)


