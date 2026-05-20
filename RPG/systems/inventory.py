from systems.Items import Weapon, Armor, Potion, Food

class Inventory:
  def __init__(self):
    self.equipped = {
      "weapon": None,
      "armor": None
    }
    self.potion = []
    self.max_potions = 100

    self.slots = [None] * 32

  def equipp(self, item, player):
    if  ininstance(item, Weapon):
      if player.stats.level < item.required_level:
        print(f"Need {item.required_level} for equip")
        return False
      self.equipped["weapon"] = item
      print(f"{item.name} equipped")
      return True
    elif isinstance(item, Armor):
      if player.stats.level < item.required_level:
        print(f"Need {item.required_level} for equip")
      self.equipped["armor"] = item
      print(f"{item.name} equipped")
      return True
    return False
    
  def unequip(self, potion):
    if self.equipped[slot]:
      item = self.equipped[slot]
      self.equipped[slot] = None
      self.add_item(item)
      print(f"Removed: {item.name}")
      
  def add_potion(self, potion):
        if len(self.potions) < self.max_potions:
            self.potions.append(potion)
            return True
        print("Potion is full!")
        return False
    
    def use_potion(self, player):
        if not self.potions:
            print("Нет зелий!")
            return False
        potion = self.potions.pop(0)
        player.stats.heal(potion.health_restore if hasattr(potion, 'health_restore') else 0)
        player.stats.current_mana = min(
            player.stats.max_mana,
            player.stats.current_mana + (potion.mana_restore if hasattr(potion, 'mana_restore') else 0)
        )
        print(f"Used: {potion.name}")
        return True
    
    def add_item(self, item):
        for i, slot in enumerate(self.slots):
            if slot is None:
                self.slots[i] = item
                return True
        print("Inventory is full!")
        return False
    
    def remove_item(self, index):
        if 0 <= index < len(self.slots) and self.slots[index]:
            item = self.slots[index]
            self.slots[index] = None
            return item
        return None
    
    def show_inventory(self):
        print("=== Inventory ===")
        print(f"Weapon: {self.equipped['weapon'].name if self.equipped['weapon'] else 'пусто'}")
        print(f"Armor: {self.equipped['armor'].name if self.equipped['armor'] else 'пусто'}")
        print(f"Potion: {len(self.potions)}/{self.max_potions}")
        print("Itmes:")
        for i, item in enumerate(self.slots):
            if item:
                print(f"  [{i}] {item.name}")
