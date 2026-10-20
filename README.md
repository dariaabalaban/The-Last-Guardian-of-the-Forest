# The Last Guardian of the Forest

A text-based RPG adventure written in Python.

## Story

Lost in unfamiliar lands, the player arrives at a mysterious village hidden deep within an ancient forest.

The villagers live in fear of a strange corruption spreading through the woods. Creatures have become hostile, travelers disappear without a trace, and an ancient spirit suffers somewhere in the darkness.

To restore balance, the player must collect three magical artifacts, craft the legendary Staff of Life, and uncover the truth behind the curse threatening the forest.

---

## Gameplay Features

* Turn-based combat system
* Multiple explorable locations
* Story-driven events and player choices
* Inventory and weapon system
* Artifact collection
* Staff of Life crafting system
* Random healing loot generator
* Save and load functionality
* Multiple enemy encounters
* Final boss encounter and ending

---

## Locations

### Elven Village

A peaceful settlement hiding a dark secret.

### Dark Forest

A dangerous forest filled with monsters and mysteries.

### Spider Cave

Home of a giant spider guarding a powerful item.

### Ancient Ruins

Ancient ruins where a mysterious owl tests the player's wisdom.

### Dead Lake

A cursed lake inhabited by deadly creatures.

### Heart Tree

The final location where the fate of the forest is decided.

---

## Enemies

* Forest Goblin
* Shadow Wolf
* Acromantul
* Siren
* Sea Whip

Each enemy has unique health and damage values.

---

## Python Features Used

This project demonstrates the use of:

* Object-Oriented Programming (Classes and Objects)
* Functions
* Lambda Function
* Custom Decorator
* Custom Exceptions
* Lists, Dictionaries, and Sets
* Dictionary Comprehensions
* Generator Function
* JSON Serialization
* File Handling with Context Managers (`with`)
* Regular Expressions
* Modular Project Structure

---

## Save System

Game progress is automatically stored in:

```text
data/save.json
```

The player can continue the adventure later using the **Load Game** option from the main menu.

---

## How to Run

### Requirements

* Python 3.10+

### Run the Game

```bash
python main.py
```

---

## Project Structure

```text
RPG_Project/
│
├── main.py
├── README.md
│
├── data/
│   └── save.json
│
├── game/
│   ├── battle.py
│   ├── events.py
│   ├── game_loop.py
│   └── locations.py
│
├── models/
│   ├── enemy.py
│   ├── items.py
│   └── player.py
│
├── storage/
│   └── save_load.py
│
├── ui/
│   └── menu.py
│
└── utils/
    ├── exceptions.py
    ├── helpers.py
    └── logger.py
```
### Modules

#### game
Contains the core gameplay logic, battles, events, locations, and the main game loop.

#### models
Contains game entities such as Player, Enemy, and Item classes.

#### storage
Handles saving and loading game progress using JSON.

#### ui
Contains menu and user interaction functionality.

#### utils
Contains helper functions, custom exceptions, and decorators/logging utilities.

#### main.py
Application entry point.

---

## Project Goal

The goal of this project was to create a complete text-based RPG game while demonstrating fundamental Python concepts, including object-oriented programming, decorators, generators, exception handling, JSON serialization, regular expressions, and modular project organization.

---

## Author

Created by **Daria Balaban** as a Python Final Project.
