#usecase4
while position < target:
    dice_roll = random.randint(1, 6)  
    count += 1
   
    event = random.randint(1, 3)
    position,event_name = moving(event, position, dice_roll)
    

    if position > target:
        position -= dice_roll 
    elif position == target:
        print("Win!")
        break


