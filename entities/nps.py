from .BaseEntity import *

class NPS(BaseEntity):
    def __init__(self, id, name, image, pos):
        super().__init__(id, name, image, pos)
        
    def entity_type(self):
        return "NPS"
    
    def entity_info(self):
        return (f"ID: {self.id}"
        f"Name: {self.name}"
        f"Image: {self.image}"
        f"Shop: {self.shop}")
    
class Banker(NPS):
    def __init__(self, id, name, image,pos):
        super().__init__(id, name, image, pos)
        self.balance = 0
        self.storage = []

    def get_balance(self):
        return self.balance

    def withdraw(self, player):
        if self.balance >= player.gold:
            self.balance -= player.gold
            return(f"Your current balance is {self.balance}")
        else:
            return("You don't have enough gold")

    def deposit(self, player):
        if player.gold > 0:
            self.balance += player.gold
            return(f"Your current balance is {self.balance}")
        else:
            return("Error")

class Shoper(NPS):
    def __init__(self, id, name, image, pos):
        super().__init__(id, name, image, pos)
        self.shop = []

    def get_shop(self):
        return self.shop
    
    def add_to_shop(self, item):
        self.shop.append(item)

    def sell_item(self, item_id, player):
        for item in self.shop:
            if item["id"] == item_id:

                if player.gold < item["price"]:
                    return "Not enough gold"
                
                
                player.gold -= item["price"]

                player.inventory.append(item)

                return f"Player bought {item['name']}"
                
        return "Item not found"
    
    def buy_item(self, item_id, player, scam = 0.75):
        for item in self._shop:

            if item["id"] == item_id:

                sell_price = int(item["price"] * scam)
                
                player.gold += sell_price

                player.inventory.remove(item)

                return f"Sold {item['name']}"
            
        return "Item not found"


nps = {}
def add_nps(name, object):
    nps[name] = object
