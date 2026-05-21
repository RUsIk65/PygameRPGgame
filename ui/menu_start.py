import pygame
from menu import Menu
from ..main import main1


pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("RPG MENU")

font = pygame.font.SysFont(None, 50)

clock = pygame.time.Clock()


menu = Menu()

running = True

while running:

    screen.fill('#71ddee')


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:


            if event.key == pygame.K_UP:
                menu.move_up()

            if event.key == pygame.K_DOWN:
                menu.move_down()

            if event.key == pygame.K_RETURN:

                action = menu.select()

                print("Selected:", action)
                match action:
                    case "start":
                        main1()
                    case "setting":
                        running = False
                    case "67":
                        pass
                # если выйти
                if action == "Exit":
                    running = False

    
    menu.draw(screen, font)

    pygame.display.update()
    clock.tick(60)

pygame.quit()