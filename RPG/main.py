import pygame
from systems.Items import *
from database.json_loader import *
    
load_items_from_json("data/items.json")
load_entities_from_json("data/entity.json")

print(type(potions[0].image))
print(potions[0].image)

pot = pygame.image.load(potions[0].image)

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
        screen.blit(pot, (100, 100))
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()