import re
import random


def get_choice(valid_choices):
    while True:
        choice = input("> Choose option: ")
        if choice in valid_choices:
            return choice
        print(
            f"Please choose one of: "
            f"{', '.join(valid_choices)}"
        )



def get_player_name():
    while True:
        name = input("Enter your name: ")
        if re.fullmatch(r"[A-Za-z ]{3,15}", name):
            return name
        print(
            "Name must contain only letters "
            "and be 3-15 characters long."
        )


def show_text(text):
    print(text)
    input("\n...")


def healing_loot():

    loot = [
        ("Forest Berry", 5),
        ("Healing Herb", 10),
        ("Red Mushroom", 15),
        ("Ancient Elixir", 25),
        (None, 0)
    ]

    while True:
        yield random.choice(loot)

loot_generator = healing_loot()


