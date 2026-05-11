import pygame
import sys
import settings
from core.state_manager import StateManager

# Сцены (пока что просто есть, потом надо будет добавить)
from ui.menu import MenuState


class Game:
    def __init__(self):
        pygame.init()

        # Окно
        self.screen = pygame.display.set_mode(
            (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
        )
        pygame.display.set_caption(settings.SCREEN_TITLE)

        self.clock = pygame.time.Clock()
        self.running = True

        # Менеджер состояний
        self.state_manager = StateManager()
        self.state_manager.add_state("menu", MenuState(self.state_manager))
    
        # self.state_manager.add_state("game",  GameState(self.state_manager))
        # self.state_manager.add_state("pause", PauseState(self.state_manager))
        self.state_manager.change_state("menu")

    def run(self):
        """Главный игровой цикл"""
        while self.running:
            ### События 
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.state_manager.handle_events(events)

            ### Обновление 
            self.state_manager.update()

            ### Отрисовка 
            self.screen.fill(settings.BLACK)
            self.state_manager.draw(self.screen)
            pygame.display.flip()

            ### FPS 
            self.clock.tick(settings.FPS)

        pygame.quit()
        sys.exit()