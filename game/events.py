from utils.exceptions import GameOverException
from game.battle import Battles
from models.enemy import Enemy
from game.locations import locations
from utils.helpers import *
import os
from models.items import Item
from utils.helpers import show_text
from utils import logger


def refuge_event(player):
    show_text(
    "A frightened refugee sits beside a small fire.\n"
    "His hands tremble as he stares into the flames."
    )
    show_text('"Stay away... stay away from the woods..."')
    print("-----------------------")
    print("1. Approach him")
    print("2. Leave")
    print("-----------------------")
    choice1 = get_choice(("1", "2"))
    if choice1 == "2":
        return
    show_text("You approach the frightened traveler.")
    print(
        f'\n{player.name}: "Are you alright?"'
    )
    show_text(
        'The refugee slowly looks up.\n'
        '"No... none of us are."'
    )
    show_text(
        '"Something has awakened beyond the village.\n'
        'People have begun to disappear."'
    )
    print("-----------------------")
    print("1. Ask what happened")
    print("2. Leave")
    print("-----------------------")
    choice2 = get_choice(("1", "2"))
    if choice2 == "2":
        return
    show_text(
        '"It started in the forest."\n'
        '"Strange creatures appeared among the trees."'
    )
    show_text(
        '"Hunters vanished. Then travelers.\n'
        'Soon nobody dared enter the woods."'
    )
    print("-----------------------")
    print("1. Ask for more details")
    print("2. Leave")
    print("-----------------------")
    choice3 = get_choice(("1", "2"))
    if choice3 == "2":
        return
    show_text(
        '"The forest is only the beginning."\n'
        '"There are whispers of a creature beneath the lake."'
    )
    show_text(
        '"And giant spiders have been seen dragging prey\n'
        'toward a cave hidden deep in the woods."'
    )
    show_text(
        '"A sailor once carried a harpoon capable of\n'
        'piercing monsters. He never returned from the forest."'
    )
    show_text(
        'The refugee reaches into his pack.'
    )
    knife = Item("Rusty Knife", 10)
    player.inventory.append(knife)
    show_text(
        '"Take this knife."\n'
        '"It is old, but better than fighting with bare hands."' )
    print("\n==== YOU RECEIVED RUSTY KNIFE! ====")
    player.completed_events.append("refuge_event")

def reward_emerald(player):
    show_text("\nThe owl nods.")
    show_text(
        'Owl: "You are worthy. Take this artifact.\n'
        'May its power guide you through the darkness ahead."'
    )
    player.artifacts.append("Emerald")
    print("---------YOU RECEIVED EMERALD-----------")

def owl_second_question(player):
    show_text(
        "The owl closes its glowing eyes "
        "for a moment before slowly nodding."
    )
    print(
        'Owl: "What should guide a person '
        'through the darkest times?"'
    )
    print("----------------------------")
    print("1. Fear")
    print("2. Power")
    print("3. Hope")
    print("----------------------------")
    answer = get_choice(("1", "2", "3"))
    if answer == "3":
        reward_emerald(player)
    else:
        show_text("\nThe owl spreads its wings.")
        print('Owl: "You are not ready"')

def owl_first_question(player):
    show_text(
        'Owl: "Then the trial begins. '
        'One false answer may seal your fate forever."'
    )
    print(
        'Owl: "First question:\n'
        'If your village stood on the edge of destruction,\n'
        'what would you do?"'
    )
    print("----------------------------")
    print("1. Save only yourself")
    print("2. Protect the innocent")
    print("3. Run from danger")
    print("----------------------------")
    answer = get_choice(("1", "2", "3"))
    if answer in ("1", "3"):
        print("\nThe owl spreads its wings.")
        print('"Owl: You are not ready"')
        return
    owl_second_question(player)

def owl_trial(player):
    show_text("------Big owl appear in front of you--------")
    print(
        '"Owl: Greetings, wandering soul.\n'
        'Answer my questions wisely, and the path '
        'to your desire shall open before you."'
    )
    print("--------------")
    print("1. Run away")
    print("2. Stay")
    print("--------------")
    answer = get_choice(("1", "2"))
    if answer == "1":
        print(
            "Owl: You fled from the trial. "
            "The owl disappeared into oblivion, "
            "taking Emerald with it."
        )
        return
    owl_first_question(player)

def owl_event(player):
    player.completed_events.append("owl_event")

    print("--------------------------")
    print(" > Someone watches you.....")
    print("1. Ignore")
    print("2. Ask who's here")
    print("--------------------------")

    answer = get_choice(("1", "2"))

    if answer == "2":
        owl_trial(player)


def staff_branch_event(player):
    show_text(
        f"As {player.name} walks through the forest, "
        f"something catches their eye."
    )
    show_text(
        "Among the roots of an ancient tree lies a perfectly \n"
        "straight branch, untouched by time.")
    show_text("Its wood feels surprisingly light and warm.")
    staff = Item("Wooden Staff", 0)
    player.inventory.append(staff)
    print("\n==== YOU RECEIVED WOODEN STAFF! ====")
    show_text(
        "It is useless as a weapon, but it feels important."
    )
    player.completed_events.append("staff_branch_event")

def owl2_event(player):
    show_text("")
    show_text("----The owl is already waiting for you.----")
    show_text("Owl: I expected your return.")
    show_text("Owl: Failure is not the end of the path.\n"
              "Only those who return after falling can truly grow.")
    print("Owl: Tell me, traveler. What is stronger:")
    print("---------------------------")
    print("fear of darkness, or hope for tomorrow?\n"
          "1. Fear\n"
          "2. Hope"
          )
    print("---------------------------")
    command = get_choice(("1", "2"))
    if command == "1":
        print("--- The owl spreads its wings.---")
        print("Owl: You still have much to learn.")
    elif command == "2":
        show_text("Owl: Wisdom is not never failing.\n"
                  "Wisdom is returning after failure.")
        print("----YOU RECEIVED EMERALD----")
        player.artifacts.append("Emerald")
        player.completed_events.append("owl2_event")


def siren_event(player):
    show_text("The song is strangely comforting.")
    print("---------------------------")
    print("\n1. Listen to the song")
    print("2. Cover your ears")
    print("---------------------------")
    choice = get_choice(("1", "2"))
    if choice == "1":
        show_text("You stop and listen.")
        show_text("The melody grows louder and louder.")
        show_text("Your mind becomes clouded.")
        player.hp -= 10
        show_text("----You lose 10 HP----")
    elif choice == "2":
        show_text("You cover your ears and resist the song.")
    show_text("A figure slowly rises from the water.")
    siren = Enemy.create_enemy(locations["dead_lake"]["enemies"][0])
    Battles.fight(player, siren)
    show_text(
        "The siren falls back into the dark water.")

def sea_whip_event(player):
    show_text("The water beneath your boat begins to churn violently.\n"
              " A massive shadow circles below.")
    show_text("Suddenly, a monstrous creature bursts from the depths.\n"
              " The Sea Whip has appeared!")
    has_harpoon = any(
        item.name == "Harpoon"
        for item in player.inventory
    )
    if has_harpoon:
        player.choose_weapon()
    if (
            not has_harpoon
            or player.weapon is None
            or player.weapon.name != "Harpoon"
    ):
        show_text(
            "You desperately search for a way to fight back,\n"
            "but nothing you have can harm the creature."
        )
        show_text(
            "The Sea Whip crashes into the side of your boat."
        )
        show_text(
            "The vessel overturns and you are thrown into the freezing water."
        )
        raise GameOverException("GAME OVER")
    show_text(
        "The Sea Whip rises from the depths, towering above your small boat.\n"
        "Waves crash against the sides as the creature lets out a deafening roar.")
    show_text("You grip the harpoon tightly. The monster moves too fast to aim\n"
              "directly at its weak spot.")
    show_text("You take a deep breath and try to predict its movement.")
    print("------------------------")
    print("\nChoose the angle of your shot:")
    print("1. 30°")
    print("2. 45°")
    print("3. 60°")
    print("------------------------")
    angle = get_choice(("1", "2", "3"))
    correct_angle = str(random.randint(1, 3))
    if angle == correct_angle:
        aquamarine_event(player)
    else:
        show_text("The harpoon cuts through the air and disappears into the lake.")
        show_text("The Sea Whip circles the boat, preparing to attack again.")
        print("------------------------")
        print("\nChoose the angle of your shot:")
        print("1. 30°")
        print("2. 45°")
        print("3. 60°")
        print("------------------------")
        second_angle = get_choice(("1", "2", "3"))
        if second_angle == correct_angle:
            aquamarine_event(player)
        else:
            show_text("The Sea Whip crashes into the boat with incredible force.")
            show_text("The vessel overturns and disappears beneath the water.")
            raise GameOverException("\n------ GAME OVER ------")


def aquamarine_event(player):
    show_text("The harpoon flies through the air and strikes the creature.")
    show_text("The Sea Whip lets out a terrible scream and thrashes wildly in the water.")
    show_text("The wounded creature slowly sinks beneath the surface.")
    show_text("You approach the floating body and cut open its stomach.\n"
              "Inside, something glows with a blue light.")
    print("\n------ YOU RECEIVED AQUAMARINE ------")
    player.artifacts.append("Aquamarine")
    sea_whip = locations["dead_lake"]["enemies"][1]
    player.kills[sea_whip["name"]] = sea_whip["damage"]


def dead_lake_event(player):
    show_text("As you approach the Dead Lake, an eerie silence surrounds you.")
    show_text("The water is perfectly still....")
    show_text("Walking along the shore of the Dead Lake, you notice an old abandoned \n"
              "boat half buried in the sand.\n"
              "Its wood is rotten, and strange claw marks cover its sides.")
    show_text("Despite its condition, the boat still seems capable of floating. \nThe dark waters ahead are calm, but an uneasy feeling settles in your chest.")
    print('-----------------------')
    print("1. Sail into the lake")
    print("2. Leave")
    print('-----------------------')
    choice = get_choice(("1", "2"))
    if choice == "2":
        return
    elif choice == "1":
        show_text("You push the boat into the water and begin rowing.\n"
                  "The further you travel, the quieter the world becomes.")
        show_text("Soon a beautiful melody reaches your ears.\n"
                  "The voice is enchanting, almost hypnotic.")
        siren_event(player)
        show_text("After dealing with the siren, you continue deeper into the lake.\n"
                  " The water beneath the boat suddenly begins to churn.\n")
        show_text("Something massive moves below you.\n"
                  "The boat rocks violently as a monstrous creature rises from the depths.")
        sea_whip_event(player)
        player.completed_events.append("dead_lake_event")




def spider_event(player):
    show_text(
        "Following the refugee's directions,\n"
        "you venture deep into the Dark Forest."
    )
    show_text(
        "After hours of wandering,\n"
        "you discover a cave covered in thick spider webs."
    )
    show_text(
        "The remains of several travelers lie near the entrance."
    )
    show_text(
        "Among the bones,\n"
        "you notice fragments of fishing gear."
    )
    show_text(
        '"This must be the place..."'
    )
    print("\n1. Enter the cave")
    print("2. Leave")
    choice = get_choice(("1", "2"))
    if choice == "2":
        return
    elif choice == "1":
        show_text("A giant spider suddenly descends from the ceiling!")
        spider = Enemy.create_enemy(locations["spider_cave"]["enemies"][0])
        Battles.fight(player, spider)
        print("The monster collapses to the ground.")
        show_text(
            "Searching the cave, you discover a skeleton\n"
            "wrapped in ancient webs."
        )
        print("Clutched in its hands is an old but sturdy harpoon." )
        show_text("====YOU RECEIVED HARPOON!====")
        player.inventory.append( Item("Harpoon", 35) )
        player.completed_events.append("spider_event")
        player.kills[spider.name] = spider.damage





def deer_event():
    show_text(
        "In the distance, through the thick fog,\n"
        "you noticed something standing out from the surrounding forest.\n"
        "A faint glow surrounded it, drawing your attention."
    )
    show_text(
        "Curious, you moved closer. As the mist slowly parted,\n"
        "you saw a magnificent deer.\n"
        "Thick roots had wrapped themselves around its body, holding it prisoner.\n"
        "One of its antlers was broken, and from the crack a dark black \n"
        "substance slowly dripped onto the ground."
    )
    show_text(
        "You took a cautious step forward,\n"
        "but suddenly the deer let out a deep growl.\n"
        "For a moment you froze."
    )
    show_text(
        'Then you remembered the last words of the refugee:\n'
        '----"The Staff of Life cannot kill. It heals. It brings hope"----'
    )
    show_text(
        "Standing before the suffering creature trapped within its own forest,\n"
        "you finally understood. This was where it had all begun.\n"
        "The deer was the Spirit of the Forest."
    )
    show_text(
        "You raised the Staff of Life.\n"
        "Immediately, the staff began to shine,\n"
        "and streams of warm light flowed from its tip towards the wounded spirit."
    )
    show_text(
        "The black liquid stopped seeping from the broken antler.\n"
        "The twisted roots slowly loosened their grip,\n"
        "and the dark vines covering the deer's body began to wither and disappear."
    )
    show_text(
        "For the first time, the creature's eyes were calm.\n"
        "In them, you saw gratitude."
    )
    show_text(
        "A moment later, the deer stepped forward and vanished into countless particles of light.\n"
        "At the same time, the dark clouds above the forest began to dissolve,\n"
        "and sunlight broke through the sky."
    )
    show_text(
        "The wind carried away the last traces of corruption.\n"
        "From their burrows emerged rabbits and other small animals.\n"
        "Birds returned to the trees."
    )
    show_text(
        "The forest was alive again.\n"
        "Balance had been restored."
    )

def heart_tree(player):
    if any(item.name == "Staff of Life" for item in player.inventory):
        player.weapon = next(
            item
            for item in player.inventory
            if item.name == "Staff of Life"
        )
        deer_event()
        victory_event(player)
    else:
        show_text("The wounded spirit watches you from the distance." )
        show_text("Without the Staff of Life, there is nothing you can do.")

def victory_event(player):
    show_text("==========YOU WIN===========")
    player.show_stats()
    print("\nArtifacts:")
    for artifact in player.artifacts:
        print(f"- {artifact}")
    print("\nInventory:")
    for item in player.inventory:
        print(f"- {item.name}")

    strongest_enemy = max(
        player.kills.items(),
        key=lambda x: x[1]
    )[0]
    show_text(
        f"Strongest defeated enemy: "
        f"{strongest_enemy} "
        f"({player.kills[strongest_enemy]} damage)"
    )
    show_text(f"\nBattles completed: {logger.battle_count}")
    show_text("=========CONGRATULATIONS==========")
    if os.path.exists("data/save.json"):
        os.remove("data/save.json")
    print("\n1. Start New Game")
    print("2. Exit")
    choice = get_choice(("1", "2"))
    if choice == "1":
        return "restart"
    elif choice == "2":
        exit()

def game_over_menu():
    print("\n========== GAME OVER ==========")
    print("1. Start New Game")
    print("2. Exit")
    choice = get_choice(("1", "2"))
    return choice

def wolf_event(player):
    show_text("You notice large paw prints in the mud.")
    show_text("The tracks lead deeper into the forest.\nSuddenly, a low growl echoes between the trees.")
    show_text("A Shadow Wolf steps out of the darkness.")
    print("---------------------")
    print("1. Fight")
    print("2. Run away")
    print("---------------------")
    choice = get_choice(("1", "2"))
    if choice == "1":
        wolf = Enemy.create_enemy(locations["dark_forest"]["enemies"][1])
        Battles.fight(player, wolf)
        show_text("The beast collapses to the ground.")
        show_text("As its body fades into black mist, something red glitters beneath it.")
        print("\n=======YOU RECEIVED RUBY!========")
        player.artifacts.append("Ruby")
        player.kills[wolf.name] = wolf.damage
        player.completed_events.append("wolf_event")
    elif choice == "2":
        show_text("You turn and run.")
        show_text("But the Shadow Wolf is faster...")
        show_text("Before you can escape, the beast lunges \nforward and tears into your shoulder.")
        player.hp -= 15
        show_text("You manage to escape, but the wound burns with pain.")
        print("\n----You lost 15 HP----")

def gnome_event(player):
    show_text("You spot a forest gnome carrying a basket full of mushrooms.")
    show_text("The gnome notices you and immediately hides the basket behind his back.")
    print("--------------------")
    print("\n1. Attack the gnome")
    print("2. Leave")
    print("--------------------")
    choice = get_choice(("1", "2"))
    if choice == "1":
        gnome = Enemy.create_enemy(locations["dark_forest"]["enemies"][0])
        Battles.fight(player, gnome)
        show_text("The frightened gnome drops his basket and runs away.")
        show_text("You take the mushrooms.")
        player.hp += 15
        print("\nYou restored 15 HP.")
        player.kills[gnome.name] = gnome.damage
    elif choice == "2":
        show_text("You decide to leave the gnome alone.")







