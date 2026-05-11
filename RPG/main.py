import pygame
from systems.Items import *
from entities import *
from database.json_loader import *
    
load_items_from_json("data/items.json")
load_entities_from_json("data/entity.json")

nps1 = pygame.image.load(nps[0].image)
nps2 = pygame.image.load(nps[1].image)
nps3 = pygame.image.load(nps[2].image)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("RPG Game")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        screen.fill((0, 0, 0))
        screen.blit(nps1, (300, 100))        
        screen.blit(nps2, (400, 100))
        screen.blit(nps3, (500, 100))
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()