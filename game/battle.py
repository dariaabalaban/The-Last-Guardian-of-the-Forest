import random
from utils.exceptions import GameOverException
from utils.logger import  battle_log
from utils.helpers import loot_generator, show_text, get_choice



class Battles:
    @staticmethod
    @battle_log
    def fight(player, enemy):
        if player.inventory:
            player.choose_weapon()
        damage = player.damage
        if player.weapon:
            damage += player.weapon.damage
        print(f" A wild {enemy.name} appears! ")
        while player.hp > 0 and enemy.hp > 0:
            print("-------------------------------")
            print(f"{player.name} HP: {player.hp} ")
            print(f"{enemy.name} HP: {enemy.hp}")
            print("-------------------------------")

            print("\n ---- YOUR TURN -----")
            print("1. Attack")
            print("2. Defend ")
            print("3. Dodge")
            print("4. Counterattack")
            player_action = get_choice(("1", "2", "3", "4"))
            enemy_action = random.randint(1, 3)
            if player_action == "1" and enemy_action == 1:
                print("\n Both attack!")
                player.attack(enemy)
                enemy.attack(player)
            elif player_action == "1" and enemy_action == 2:
                print(f"{enemy.name} blocked your attack!")
            elif player_action == "2"  and enemy_action == 1:
                print(f"You block {enemy.name} attack")
            elif player_action == "3" and enemy_action == 1:
                dodge = random.randint(1, 100)
                if dodge <= 50:
                    print(f" You dodged the attack!")
                else:
                    enemy.attack(player)
            elif player_action == "1" and enemy_action == 3:
                dodge = random.randint(1, 100)
                if dodge <= 50:
                    print(f" {enemy.name} dodge the attack!")
                else:
                    player.attack(enemy)
            elif player_action == "4" and enemy_action == 1:
                counter_damage = damage + 10
                actual_damage = min(counter_damage, enemy.hp)
                enemy.hp -= actual_damage
                print(f"You countered the attack! \n {enemy.name} loses {actual_damage} HP")
            elif player_action == "4":
                player.hp -= 5
                print(f"You failed your counterattack and lose 5 HP!")
            elif player_action == "2" and enemy_action == 2:
                print("Both fighters remain on guard.")

            elif player_action == "2" and enemy_action == 3:
                print(f"{enemy.name} waits for an opening.")

            elif player_action == "3" and enemy_action == 2:
                print("You look for a chance to strike.")

            elif player_action == "3" and enemy_action == 3:
                print("Both fighters circle each other carefully.")


        if player.hp <= 0:
            print("---YOU LOSE!---")
            raise GameOverException("\n --------GAME OVER---------")
        elif enemy.hp <= 0:
            print("------YOU WIN ------")
            player.damage += 10
            if enemy.hp <= 0:

                show_text(
                    f"With the enemy defeated, "
                    f"{player.name} takes a moment "
                    f"to search the area."
                )
                food_name, hp = next(loot_generator)
                if food_name:
                    print(
                        f"{player.name} found {food_name}."
                    )
                    print(f"\n+{hp} HP")
                    player.hp = min(player.hp + hp, 100)
                else:
                    print(
                        "Nothing useful was found."
                    )
                return







