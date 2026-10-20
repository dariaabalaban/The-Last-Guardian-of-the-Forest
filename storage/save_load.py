import json
from models.player import Player
from models.items import Item


def save_game(player):
    data = {
        "name": player.name,
        "hp": player.hp,
        "damage": player.damage,
        "location": player.location,
        "artifacts": player.artifacts,
        "completed_events": player.completed_events,
        "inventory": [item.name for item in player.inventory]
    }
    with open("data/save.json", "w") as save_file:
        json.dump(data, save_file)
    print("\n------------------")
    print("---Game saved!---")
    print("------------------")

def load_game():
    try:

        with open("data/save.json", "r") as file:
            data = json.load(file)
            player = Player(data["name"])
            player.hp = data["hp"]
            player.damage = data["damage"]
            player.location = data["location"]
            player.artifacts = data["artifacts"]
            player.inventory = []
            for item_name in data["inventory"]:
                if item_name == "Harpoon":
                    player.inventory.append(
                        Item("Harpoon", 30))
                elif item_name == "Wooden Staff":
                    player.inventory.append(
                        Item("Wooden Staff", 10))
                elif item_name == "Staff of Life":
                    player.inventory.append(
                        Item("Staff of Life", 100))
            player.completed_events = data["completed_events"]
            print("\n------------------")
            print("   Game loaded!")
            print("------------------")
            return player

    except FileNotFoundError:
        print("\nNo saved game found!")
        return None


