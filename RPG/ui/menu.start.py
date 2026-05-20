import pygame
from ui.menu import Menu

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("RPG MENU")
font = pygame.font.SysFont(None, 50)
clock = pygame.time.Clock()


# MENU

menu = Menu()
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # КЛАВИАТУРА
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                menu.move_up()
            if event.key == pygame.K_DOWN:
                menu.move_down()
            if event.key == pygame.K_RETURN:
                action = menu.select()
                if action == "Start":
                    # TODO: запустить игру
                    pass
                elif action == "Exit":
                    running = False

        # МЫШЬ
        if event.type == pygame.MOUSEMOTION:
            menu.handle_mouse_motion(event.pos)


        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            action = menu.handle_mouse_click(event.pos)
            if action == "Start":
                # TODO: запустить игру
                pass
            elif action == "Exit":
                running = False

    # DRAW

    menu.draw(screen, font)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
