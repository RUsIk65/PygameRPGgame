import json
import os
from systems.Items import *
_DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "items.json")
try:
    with open(_DATA_PATH, "r", encoding="utf-8") as f:
        ITEMS_DB = {item["id"]: item for item in json.load(f) if "id" in item}
except FileNotFoundError:
    ITEMS_DB = {}


class Inventory:
    MAX_SIZE = 20  

    def __init__(self):
        self.items: list[Item] = []  
        self.equipped: dict[str, Item | None] = {
            "weapon":  None,
            "armor":   None,
        }


    def add_item(self, item: Item) -> bool:
        if len(self.items) >= self.MAX_SIZE:
            return False
        self.items.append(item)
        return True

    def remove_item(self, item: Item):
        if item in self.items:
            self.items.remove(item)

    def equip(self, item: Item) -> Item | None:
        slot = item.item_type().lower() 
        if slot not in self.equipped:
            return None

        old_item = self.equipped[slot]
        self.equipped[slot] = item
        self.remove_item(item)             
        if old_item:
            self.items.append(old_item)    
        return old_item

    def unequip(self, slot: str) -> bool:
        item = self.equipped.get(slot)
        if item and len(self.items) < self.MAX_SIZE:
            self.items.append(item)
            self.equipped[slot] = None
            return True
        return False

    def get_bonus_stats(self) -> dict:
        bonus = {"attack": 0, "defense": 0, "speed": 0, "hp": 0}
        weapon = self.equipped.get("weapon")
        armor = self.equipped.get("armor")
        
        if weapon and hasattr(weapon, "damage"):
            bonus["attack"] += weapon.damage
        if armor and hasattr(armor, "defense"):
            bonus["defense"] += armor.defense
            
        return bonus

    def get_item_at_index(self, index: int) -> Item | None:
        if 0 <= index < len(self.items):
            return self.items[index]
        return None

    @property
    def count(self) -> int:
        return len(self.items)
