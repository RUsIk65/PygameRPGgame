import pygame

from systems.stats import Stats
from systems.inventory import Inventory

from ui.bars import Bar
from ui.inventory_ui import InventoryUI


pygame.init()

# SCREEN

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("RPG GAME")

font = pygame.font.SysFont(None, 35)

clock = pygame.time.Clock()

running = True


# PLAYER


player = Stats()


# INVENTORY


inventory = Inventory()

# test items
class Item:
    def __init__(self, name):
        self.name = name


inventory.add_item(Item("Sword"))
inventory.add_item(Item("Potion"))
inventory.add_item(Item("Bow"))

inventory_ui = InventoryUI(inventory)

show_inventory = False

# BARS

hp_bar = Bar(
    50,
    50,
    300,
    25,
    player.max_hp,
    (255, 0, 0)
)

mana_bar = Bar(
    50,
    90,
    300,
    25,
    player.max_mana,
    (0, 100, 255)
)

xp_bar = Bar(
    50,
    130,
    300,
    20,
    player.xp_to_next_level,
    (180, 0, 255)
)
# GAME LOOP

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # open inventory
            if event.key == pygame.K_i:
                show_inventory = not show_inventory


    # DRAW
    
    screen.fill((0, 0, 0))

    # bars
    hp_bar.draw(screen, player.current_hp)

    mana_bar.draw(screen, player.current_mana)

    xp_bar.draw(screen, player.xp)

    # level text
    level_text = font.render(
        f"Level: {player.level}",
        True,
        (255, 255, 255)
    )

    screen.blit(level_text, (400, 50))

    # inventory
    if show_inventory:
        inventory_ui.draw(screen, font)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
