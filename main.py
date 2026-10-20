from game.game_loop import start_game
from utils.exceptions import GameOverException
import os
from utils.helpers import get_choice


while True:
    try:
        start_game()
    except GameOverException as e:
        print(e)
        if os.path.exists("data/save.json"):
            os.remove("data/save.json")
        print("\n1. Menu")
        print("2. Exit")
        choice = get_choice(("1", "2"))
        if choice == "2":
            break
        elif choice == "1":
            continue


