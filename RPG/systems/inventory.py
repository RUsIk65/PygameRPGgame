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
