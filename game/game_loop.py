from game.locations import*
from game.events import*
from utils.exceptions import *
from ui.menu import main_menu
from storage.save_load import save_game


def start_game():
    try:
        player = main_menu()
    except GameOverException as e:
        print(e)


    while True:

        cur_location = locations[player.location]
        print('\n===================================================================================')
        print(f"Current location of {player.name} : {cur_location['name']}")
        print('===================================================================================')
        if player.location == 'village':
            if "village_intro" not in player.completed_events:
                village_intro(player)

            if "refuge_event" not in player.completed_events:
                refuge_event(player)

        elif player.location == "dark_forest":
            if "forest_intro" not in player.completed_events:
                forest_intro(player)
            if "Ruby" not in player.artifacts:
                wolf_event(player)

            else:
                if random.randint(1, 3) == 1:
                    gnome_event(player)
            if "staff_branch_event" not in player.completed_events:
                staff_branch_event(player)
            #ANCIENT RUINS

        elif player.location == "ancient_ruins":
            if "ancient_ruins_intro" not in player.completed_events:
                ancient_ruins_intro(player)
            if "owl_event" not in player.completed_events:
                owl_event(player)
            elif "Emerald" not in player.artifacts:
                owl2_event(player)
        # SPIDER CAVE
        elif player.location == "spider_cave":
            if "spider_cave" not in player.completed_events:
                spider_cave(player)
            if "spider_event" not in player.completed_events:
                spider_event(player)

        # DEAD LAKE
        elif player.location == "dead_lake":
            if "dead_lake_event" not in player.completed_events:
                 dead_lake_event(player)

        # HEART TREE
        elif player.location == "heart_tree":
            heart_tree(player)
            if "victory_event" in player.completed_events:
                print("\n1. Start New Game")
                print("2. Exit")
                choice = input("> Choose option: ")
                if choice == "1":
                    player = main_menu()
                elif choice == "2":
                    exit()

        required = ["Aquamarine", "Emerald", "Ruby"]
        if (
                all(artifact in player.artifacts for artifact in required)
                and not any(item.name == "Staff of Life"
                            for item in player.inventory)
        ):
             player.craft_staff()
        save_game(player)
        print("\nAvailable directions:")
        for index, location in enumerate(
                cur_location["directories"]
        ):
            print(
                f"{index + 1}. "
                f"{locations[location]['name']}")
        choice = get_choice(
            tuple(str(i + 1) for i in range(len(cur_location["directories"]))))
        player.location = cur_location["directories"][int(choice) - 1]



