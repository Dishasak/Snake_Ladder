import random

player1 = 0
player2 = 0
count = 0
target = 100

print(f"Player1 is on the position {player1}")
print(f"Player2 is on the position {player2}")

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

while player1 < target and player2 < target:


    # Player1 turn
    dice_roll = random.randint(1, 6)
    count += 1
    print(f"Player 1 rolled: {dice_roll}")
    
    event = random.randint(1, 3)
    player1, event_name = moving(event, player1, dice_roll)
    
    if player1 < 0:
        player1 = 0
    
    print(f"Player 1 event: {event_name}, Position: {player1}")
    
    if player1 == target:
        print("Player 1 wins!")
        break
    
    # Player 2 turn
    dice_roll = random.randint(1, 6)
    count += 1
    print(f"Player 2 rolled: {dice_roll}")
    
    event = random.randint(1, 3)
    player2, event_name = moving(event, player2, dice_roll)
    
    if player2 < 0:
        player2 = 0
    
    print(f"Player 2 event: {event_name}, Position: {player2}")
    
    if player2 == target:
        print("Player 2 wins!")
        break

print(f"Game over. Number of times dice rolls: {count}")

