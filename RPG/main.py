import pygame

from systems.stats import Stats
from ui.bars import Bar


pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True


player = Stats()

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


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    hp_bar.draw(screen, player.current_hp)
    mana_bar.draw(screen, player.current_mana)
    xp_bar.draw(screen, player.xp)

    pygame.display.update()

pygame.quit()
