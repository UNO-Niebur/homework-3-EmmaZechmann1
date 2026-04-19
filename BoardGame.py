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


# Design document
# This game will be designed as a game bord similar to candy land. The board will include a forest, dungeon and a bridge. 
# The bridge will be an action that if you land on one side on the specific space you can use it to cut across the board.
# The path will be winding and will be roughly 100 spaces long. As seen above the player will go through mountiains and forests,
# some of which will have "trolls" that will keep the player their for a certain amount of turns. The game will be played by two or more players,
# where each player will roll a dice to decide how far they will go fowrward. Who ever gets to the last tile first wins.
# The data is stored in this program sort of like a dictionary, you collect data, store it then when the player moves the data changes, 
# and the old data is deleted. The main function I am using is the random function. this allows me to make a dice roll. 
