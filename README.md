Yerzat67 is here
Masnur52 also here
Ruslan69 also here
🎮 Project Overview

This is a 2D RPG game built using Python and Pygame.
The project follows a modular architecture with separated systems for gameplay, UI, entities, database logic, and world management.

The game includes:

Player progression system
Combat system
Inventory & items
NPC and enemy entities
Save/load system
Tile-based world
UI system (bars, menus, inventory)
📁 Project Structure
RPG/
│
├── main.py
│
├── systems/
│   ├── stats.py
│   ├── combat.py
│   ├── inventory.py
│   ├── Items.py
│   ├── save_system.py
│   ├── loot.py
│
├── entities/
│   ├── Player.py
│   ├── enemy.py
│   ├── nps.py
│   ├── BaseEntity.py
│
├── ui/
│   ├── menu.py
│   ├── menu.start.py
│   ├── pause_menu.py
│   ├── Bars.py
│   ├── inventory_ui.py
│
├── world/
│   ├── camera.py
│   ├── 1.tmx
│   ├── assets/
│
├── database/
│   ├── items.json / db
│   ├── entity.json / db
│   ├── items_base.py
│   ├── entity_base.py
│   ├── json_loader.py
│
├── texture/
│   ├── player/
│   ├── enemy/
│   ├── items/
│   ├── nps/
│
├── data/
│   ├── items.json
│   ├── entity.json
│   ├── shops.json
│   ├── drops.json
│
├── saves/
│   ├── savegame.json
⚔️ Core Systems
🧠 Stats System (systems/stats.py)

Handles all player attributes:

HP / Max HP
Mana / Max Mana
Attack
Defense
Speed
Charisma
XP / Level system

Supports:

stat scaling on level up
XP progression system
attribute modification
⚔️ Combat System (systems/combat.py)

Implements battle mechanics:

Damage calculation
Defense reduction
Critical hits
Dodge mechanics (speed-based)
Example logic:
Attack − Defense = base damage
Critical hit = ×2 damage
🎒 Inventory System (systems/inventory.py)

Features:

32 inventory slots
item storage system
equipment system (weapon/armor)
potion usage system

Supports:

weapons
armor
consumables
item stacking (planned/extendable)
💾 Save System (systems/save_system.py)

Uses JSON-based persistence.

Saves:

player stats
level / XP
HP / Mana
inventory
game progress

File:

saves/savegame.json
🎁 Items System (systems/Items.py)

Defines item classes:

Weapon
Armor
Potion
Food

Supports:

required level
item attributes
equip system integration
💀 Loot System (systems/loot.py)

Handles:

item drops from enemies
random loot generation
item reward system
🧍 Entities System

Located in entities/

Includes:
Player class
Enemy class
NPC system
BaseEntity parent class
Features:
movement
interaction system
combat integration
inheritance structure
🗺️ World System
world/camera.py

Handles:

camera movement
player tracking
world scrolling
Map System
TileMap (.tmx file support)
assets for environment (forest/desert)
🖥️ UI System
Implemented UI:
HP Bar
Mana Bar
XP Bar
Inventory Window
Pause Menu
Main Menu

Files:

ui/Bars.py
ui/inventory_ui.py
ui/menu.py
ui/pause_menu.py
🎮 Gameplay Features
Implemented:
player movement
combat system
enemy interaction
inventory system
leveling system
UI system
save/load system
world rendering
📊 Progression System

Player starts at level 0.

Level up rewards:
+HP
+Mana
+Attack
+Defense
+Speed

XP system controls progression speed and difficulty scaling.

🧠 OOP Design

The project is built using Object-Oriented Programming:

Principles used:
Encapsulation (Stats, Inventory)
Inheritance (Entities system)
Abstraction (system separation)
Modular architecture
🎯 Goals of the Project
Build a complete RPG architecture
Learn game development with Python
Practice OOP design
Create scalable game systems
Implement real gameplay loop
🚀 Future Improvements

Planned features:

advanced enemy AI
quests system
dialogue system
sound system
animations
combat effects (damage text, particles)
better loot system
skill system
crafting system
🏁 Conclusion

This project is a modular RPG prototype with a fully working core system including:

combat
inventory
stats
UI
save/load
world system

It is designed to be expandable into a full RPG game.
