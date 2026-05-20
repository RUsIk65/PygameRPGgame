import pygame

from systems.stats import Stats
from systems.inventory import Inventory
from systems.save_system import save_game, load_game, save_exists

from ui.Bars import Bar
from ui.inventory_ui import InventoryUI
from ui.menu import Menu

from world.camera import camera_group, load_map
from entities.Player import Player


pygame.init()

screen = pygame.display.set_mode((1500, 800))
pygame.display.set_caption("RPG GAME")
font = pygame.font.SysFont(None, 35)
clock = pygame.time.Clock()


# MENU LOOP

menu = Menu()
in_menu = True

while in_menu:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                menu.move_up()
            if event.key == pygame.K_DOWN:
                menu.move_down()
            if event.key == pygame.K_RETURN:
                action = menu.select()
                if action == "Start":
                    in_menu = False
                elif action == "Exit":
                    pygame.quit()
                    quit()

        if event.type == pygame.MOUSEMOTION:
            menu.handle_mouse_motion(event.pos)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            action = menu.handle_mouse_click(event.pos)
            if action == "Start":
                in_menu = False
            elif action == "Exit":
                pygame.quit()
                quit()

    menu.draw(screen, font)
    pygame.display.update()
    clock.tick(60)

# GAME SETUP

load_map()

player = Player(
    id=1,
    name="Hero",
    image="texture/player/Hero_idle.png",
    pos=(750, 400)
)

inventory = Inventory()

if save_exists():
    load_game(player, inventory)

inventory_ui = InventoryUI(inventory)
show_inventory = False

# BARS
mana_bar = Bar(20, 20, 250, 20, player.max_mana,          (0, 100, 255))
xp_bar   = Bar(20, 50, 250, 15, player.xp_to_next_level,  (0, 200, 50))


# GAME LOOP

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            save_game(player, inventory)
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if not show_inventory:
                player.set_target(pygame.mouse.get_pos() + camera_group.offset)

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_i:
                show_inventory = not show_inventory

            if event.key == pygame.K_F5:
                save_game(player, inventory)
                print("Игра сохранена!")

            if event.key == pygame.K_F9:
                load_game(player, inventory)
                mana_bar.max_value = player.max_mana
                xp_bar.max_value   = player.xp_to_next_level

    # UPDATE
    camera_group.update()

    # DRAW
    screen.fill((0, 0, 0))
    camera_group.kaif_draw(player)

    # BARS
    mana_bar.draw(screen, player.current_mana)
    xp_bar.draw(screen, player.xp)

    # LEVEL
    level_text = font.render(f"Level: {player.level}", True, (255, 255, 255))
    screen.blit(level_text, (280, 18))

    # HP текст
    hp_text = font.render(f"HP: {player.current_hp}/{player.max_hp}", True, (255, 80, 80))
    screen.blit(hp_text, (20, 70))

    if show_inventory:
        inventory_ui.draw(screen, font)

    pygame.display.update()
    clock.tick(60)

pygame.quit()