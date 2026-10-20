from utils.helpers import show_text


locations = {
    "village": {
        "name": "Elven Village",
        "directories" : ["dark_forest", "ancient_ruins"]

    },
    "dark_forest": {
        "name": "Dark Forest",
        "artifact" : "Ruby",
        "required_kills": 2,
        "enemies" : [
            {
                "name" : "Forest Goblin",
                "hp" : 40,
                "damage" : 12
            },
            {
                "name" : "Shadow Wolf",
                "hp" : 50,
                "damage" : 25
            },
        ],
        "directories":["village", "dead_lake", "spider_cave"]

    },
    "spider_cave" : {
            "name" : "Spider Cave",
            "west" : "dark_forest",
             "enemies" :[{
                    "name": "Acromantul",
                    "hp": 30,
                    "damage": 30
             }],
        "directories" : ["dark_forest"]
     },
    "ancient_ruins": {
        "name": "Ancient Ruins",
        "directories" : ["village"]
    },
    "dead_lake": {
        "name": "Dead Lake",
        "artifact" : "Aquamarine",
        "required_kills": 2,
        "enemies": [
            {"name" : "Siren",
             "hp" : 40,
             "damage" : 30
             },
            {"name" : "Sea Whip",
             "hp" : 70,
             "damage" : 70
             }
        ],

        "directories" : ["dark_forest", "heart_tree"]
    },
    "heart_tree": {
        "name": "Heart Tree",
        "directories": ["dead_lake"]
    },

}



def village_intro(player):
    show_text("For several days you had wandered through unknown lands.\n"
              "Lost and exhausted, you followed distant lights through the forest.\n"
              "Soon you arrived at a small village inhabited by strange creatures,"
               "more similar to gnomes than humans.")
    show_text( "At first glance the village seemed peaceful and cozy.\n"
               "Yet something felt terribly wrong.\n"
               "Villagers hurried through the streets, gathering supplies and packing their belongings.\n"
               "Fear could be seen on every face.\n")
    show_text( "Some nervously glanced toward the forest, while others whispered among themselves.\n"
               "Curious about the commotion, you decide to look around.")
    player.completed_events.append("village_intro")


def ancient_ruins_intro(player):
    show_text("Beyond the village, hidden among ancient trees, "
    "stand the ruins of a long-forgotten civilization.\n"
    "Cracked stone arches cast dark shadows across the path, "
    "and strange symbols are carved into the weathered walls.\n"
    "Somewhere in the distance, an owl watches your every step."
)
    player.completed_events.append("ancient_ruins_intro")


def forest_intro(player):
    show_text(
        "As you step into the Dark Forest, the sounds of the village fade behind you. \n"
        "The trees tower high above your head, their twisted branches blocking most of the sunlight.")
    show_text(
        "A cold wind moves through the leaves, carrying strange whispers from somewhere deep within the woods.\n"
        " The refugee's warning echoes in your mind: 'Stay away from the forest...'")

    show_text("For a moment, you wonder if you should have listened. But the path forward lies within the darkness.")
    player.completed_events.append("forest_intro")

def spider_cave(player):
    show_text("Following the refugee's directions, you venture deeper into the forest.\n"
        "Before long, you discover a cave hidden behind a curtain of thick spider webs.\n"
        "The silence around it feels unnatural.")
    show_text("Bones litter the ground near the entrance,\n"
        "and strands of web stretch between the trees like ghostly ropes.\n"
        "Something is waiting inside.")
    player.completed_events.append("spider_cave")