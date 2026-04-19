# Homework 3 - Board Game System
# Name: Emma Zechmann
# Date: 4/19/26
import random 

def loadGameData(filename):
    data = {}
    turn = None

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith("Turn:"):
                turn = line.split(":")[1].strip()
            
            elif ":" in line:
                position, value = line.split(":")
                data[int(position)] = value.strip()

    return turn, data

def displayGame(turn, data):

    print("\n===== Game State ===== ")
    print("Current Turn:", turn)
    print("-------------------------")

    for i in range(1,30):
        if i in data:
            print(f"{i}: {data[i]}")
        else: 
            print(f"{i}: Empty")

def findPlayer(data, player_name):
    for pos, value in data.items():
        if value == player_name:
            return pos

    return None 

def movePlayer(data, turn):
    pos = findPlayer(data, turn)

    if pos is None:
        print("player not found!")
        return

    roll = random.randint(1,6)
    print(f"\n{turn} rolled a {roll}!")

    new_pos = pos + roll

    print(f"{turn} moves from {pos} to {new_pos}!")
    del data [pos]
    data[new_pos] = turn


def main():
    filename = "events.txt"   
    turn, gameData = loadGameData(filename)

    while True:
        displayGame(turn, gameData)
        choice = input("\nMove player? (y/n): ").lower()

        if choice == "y":
            movePlayer(gameData, turn)
        else: 
            print("Game Ended! ")
            break


if __name__ == "__main__":
    main()
