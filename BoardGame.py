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

def saveGameData(filename, turn, data):
    with open(filename, "w") as file:
        file.write(f"Turn: {turn}\n")
        for pos in data:
            file.write(f"{pos}:{data[pos]}\n")

def displayGame(turn, data):

    print("\n===== Game State ===== ")
    print("Current Turn:", turn)
    print("-------------------------")

    for i in range(1,100):
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
        print(f"{turn} not found on board. Placing at start.")
        pos = 1
        data[pos] = turn

    roll = random.randint(1,6)
    print(f"\n{turn} rolled a {roll}!")

    new_pos = pos + roll

    if new_pos == 10:
        print("You landed on the bridge shortcut! Move forward 8 spaces.")
        new_pos +=8

    if new_pos == 15:
        print("You landed on an angry troll and he pushes you back three spaces!")
        new_pos -=3

    print(f"{turn} moves from {pos} to {new_pos}!")

    del data [pos]
    data[new_pos] = turn

    if new_pos >= 100:
        print(f"\n {turn} made it to the castle and won the game!")
        return True
    
    return False 


def main():
    filename = "events.txt"   
    turn, gameData = loadGameData(filename)

    players = ["Player1", "Player2"]

    if "Player1" not in gameData.values():
        gameData[1] = "Player1"

    if "Player2" not in gameData.values():
        gameData[1] = "Player2"

    while True:
        displayGame(turn, gameData)
        choice = input("\nMove player? (y/n): ").lower()

        if choice == "y":
            won = movePlayer(gameData, turn)

            saveGameData(filename, turn, gameData)

            if won:
                break

            current_index = players.index(turn)
            current_index = (current_index +1) % len(players)
            turn = players[current_index]

        


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
