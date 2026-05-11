import pygame
import settings


class MenuState:
    def __init__(self, state_manager):
        self.sm = state_manager
        self.font = None

    def enter(self):
        self.font = pygame.font.SysFont("Arial", 48)

    def exit(self):
        pass

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pass  # self.sm.change_state("game")

    def update(self):
        pass

    def draw(self, screen):
        text = self.font.render("Нажми Enter для старта", True, settings.WHITE)
        rect = text.get_rect(center=(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT // 2))
        screen.blit(text, rect)