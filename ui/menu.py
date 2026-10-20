from utils.helpers import get_choice
from storage.save_load import load_game
from models.player import Player
from utils.helpers import get_player_name


def main_menu():
    print("========HELLO NEW PLAYER==========")
    print('CHOSE ONE OPTION:')
    print("1. Rules")
    print("2. Load Game")
    print("3. Start a game")
    print("4. Exit")

    while True:

        choice = get_choice(("1", "2", "3", "4"))
        if choice == "1":
            print("\n=== RULES ===")
            print("Travel through locations and collect artifacts.")
            print("Fight enemies and survive dangerous encounters.")
            print("Collect all magical stones to create the Staff of Life.")
            print("Only the Staff of Life can defeat the final boss.")
            input('\n Please enter to return to the main menu:  ')

        elif choice == "2":
            player = load_game()
            if player is None:
                continue
            return player

        elif choice == "3":
            name = get_player_name()
            return Player(name)

        elif choice == "4":
            print("\n Goodbye, traveler")
            exit()

