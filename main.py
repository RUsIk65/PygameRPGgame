import pygame

from database.json_loader import load_entities_from_json, load_items_from_json

from systems.stats import Stats
from systems.inventory import Inventory
from systems.save_system import save_game, load_game, save_exists

from ui.Bars import Bar
from ui.inventory_ui import InventoryUI
from ui.menu import Menu
from ui.pause_menu import PauseMenu


from world.camera import camera_group, load_map

from entities.Player import Player
from entities import nps

from ui.pause_menu import PauseMenu


pygame.init()

screen = pygame.display.set_mode((1500, 800))
pygame.display.set_caption("RPG GAME")
font = pygame.font.SysFont(None, 35)
font_small = pygame.font.SysFont(None, 22)
clock = pygame.time.Clock()


# MENU 

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

# GAME 

load_map()

player = Player(
    id=1,
    name="Hero",
    image="texture/player/Hero_idle.png",
    pos=(200, 200)
)
load_items_from_json("data/items.json")
load_entities_from_json("data/entity.json")
    
inventory = Inventory()

if save_exists():
    load_game(player, inventory)

inventory_ui = InventoryUI(inventory)
pause_menu = PauseMenu()

mana_bar = Bar(20, 50, 200, 16, player.max_mana,          (50, 100, 255))
xp_bar   = Bar(20, 75, 200, 12, player.xp_to_next_level,  (0, 200, 50))
hp_bar = Bar(20, 25, 200, 16, player.max_hp, (220, 50, 50))



running = True

while running:

    sw, sh = screen.get_size()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            save_game(player, inventory)
            running = False

        result = pause_menu.handle_event(event, sw, sh)
        if result == "save":
            save_game(player, inventory)
            print("Игра сохранена!")
        elif result == "quit":
            save_game(player, inventory)
            running = False

        # Пока пауза открыта 
        if pause_menu.visible:
            continue

        inventory_ui.handle_event(event)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if not inventory_ui.visible:
                player.set_target(pygame.mouse.get_pos() + camera_group.offset)

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                pause_menu.toggle()

            if event.key == pygame.K_i:
                inventory_ui.toggle()

            if event.key == pygame.K_F9:
                load_game(player, inventory)
                hp_bar.max_value   = player.max_hp
                mana_bar.max_value = player.max_mana
                xp_bar.max_value   = player.xp_to_next_level

    if not pause_menu.visible:
        camera_group.update()

    # UPDATE
    screen.fill("#33C9FF")

    # DRAW
    camera_group.kaif_draw(player)

    # HUD
    pygame.draw.rect(screen, (15, 15, 20), (10, 10, 230, 95), border_radius=8)
    pygame.draw.rect(screen, (60, 60, 80), (10, 10, 230, 95), 1, border_radius=8)

    hp_label = font_small.render(
        f"HP  {player.current_hp}/{player.max_hp}", True, (255, 100, 100))
    screen.blit(hp_label, (22, 12))
    hp_bar.max_value = player.max_hp
    hp_bar.draw(screen, player.current_hp)

    mana_label = font_small.render(
        f"MP  {player.current_mana}/{player.max_mana}", True, (100, 160, 255))
    screen.blit(mana_label, (22, 37))
    mana_bar.max_value = player.max_mana
    mana_bar.draw(screen, player.current_mana)

    xp_label = font_small.render(
        f"XP  {player.xp}/{player.xp_to_next_level}", True, (100, 220, 100))
    screen.blit(xp_label, (22, 62))
    xp_bar.max_value = player.xp_to_next_level
    xp_bar.draw(screen, player.xp)

    lvl_text = font.render(f"Lv.{player.level}", True, (255, 210, 60))
    screen.blit(lvl_text, (248, 40))

    # INVENTORY
    inventory_ui.draw(screen, player)

    # PAUSE MENU (поверх всего)
    pause_menu.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()