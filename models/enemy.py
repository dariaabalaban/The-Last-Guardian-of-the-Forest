class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, player):
        player.hp -= self.damage
        print(f"{self.name} attacks {player.name}!")

    @staticmethod
    def create_enemy(enemy_data):
        return Enemy(
            enemy_data["name"],
            enemy_data["hp"],
            enemy_data["damage"]
        )


