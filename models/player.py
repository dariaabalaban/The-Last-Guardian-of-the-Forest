from models.items import Item
from utils.helpers import get_choice


class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.damage = 15
        self.inventory = []
        self.weapon = None
        self.artifacts = []
        self.kills = {}
        self.location = "village"
        self.completed_events = []

    def show_stats(self):
        print("\n -------PLAYER STATUS---------")
        print(f"Name: {self.name}")
        print(f"HP: {self.hp}")
        print(f"Damage: {self.damage}")

    def attack(self, enemy):
        damage = self.damage
        if self.weapon:
            damage += self.weapon.damage
        enemy.hp -= damage
        print(
            f"{self.name} attacks "
            f"{enemy.name} for {damage} damage!"
        )

    def craft_staff(self):
        required_artifacts = {
            "Emerald",
            "Ruby",
            "Aquamarine"

        }
        if required_artifacts.issubset(self.artifacts)  and any(
                item.name == "Wooden Staff"
                 for item in self.inventory
                ):
            self.inventory.append(Item("Staff of Life", 100))
            for item in self.inventory:
                if item.name == "Wooden Staff":
                    self.inventory.remove(item)
                    break
            print(" ---You have all the elements needed "
                  "to create the Staff of Life!---")
            print("\n The staff of life has been created!")
            return True
        else:
            print("\n You do not have the required items")
            return False

    def show_inventory(self):
        for index, item in enumerate(self.inventory):
            print(str(index + 1) + ". " + item.name)

    def equip_weapon(self, weapon):
        if weapon not in self.inventory:
            print("\n You do not have this weapon, please choose something else")
        else:
            self.weapon = weapon
            print(f"\n You equipped {weapon.name} ")

    def choose_weapon(self):
        if not self.inventory:
            print("\nYou have no weapons.")
            return
        print("\nChoose a weapon:")
        weapons = {
            str(index + 1): item
            for index, item in enumerate(self.inventory)
        }
        print("0. Nothing")
        for key, weapon in weapons.items():
            print(f"{key}. {weapon.name}")
        choice = get_choice(("0",) + tuple(weapons.keys()))
        if choice == "0":
            self.weapon = None
            print("\nYou fight with your bare hands.")
            return
        self.weapon = weapons[choice]
        print(
            f"\n{self.name} equipped "
            f"{self.weapon.name}."
        )



