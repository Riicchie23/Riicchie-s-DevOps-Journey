# Create a RPG-like game, where there's a boss and the player needs to defeat it
# Player can choose what class they want
# It will have a fixed set of skills
# Player can know how many hp the boss still has
# It will be a turn-based type of game

from pynput.keyboard import Key
import sys, time
# sys.path.append("D:/DevOps/Riicchie-s-DevOps-Journey/")
sys.path.append("E:/Projects/Riicchie-s-DevOps-Journey/")

from Python.key_reader import KeyListener
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

    def cont_func(self):
        target_key = Key.enter
        kl = KeyListener(target_key)
        try:
            kl.start_listener()
        except Exception as e:
            print(e)

    def intro_dialogue(self):
        print("This is the intro")


if __name__ == "__main__":
    rpg = RPG()

    try:
        rpg.start_game()
        rpg.intro_dialogue()
        
        rpg.cont_func()
        print("Press Enter to Continue")
        # print("Enter Action: ")
        # print("(A)ttack, (S)kills, (I)nfo, (Q)uit")

    except Exception as e:
        print(e)