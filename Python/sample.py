# Create a RPG-like game, where there's a boss and the player needs to defeat it
# Player can choose what class they want
# It will have a fixed set of skills
# Player can know how many hp the boss still has
# It will be a turn-based type of game

import sys

class RPG():
    def __init__(self):
        boss_hp = None
        player_hp = None
        is_active = None #It means the player is active
    
    def start_game(self):
        """Question to start the game
        """        
        print("Start game? (y/n)")
        if input().strip().lower() != "y":
            sys.exit()
        pass

    def intro_dialogue(self):
        pass


if __name__ == "__main__":
    rpg = RPG()

    try:
        rpg.start_game()
        print("Enter Action: ")
        print("(A)ttack, (S)kills, (I)nfo, (Q)uit")

    except Exception as e:
        print(e)