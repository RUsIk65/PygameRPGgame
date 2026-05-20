import pygame


class Menu:
    def __init__(self):
        self.selected_option = 0
        self.options = [
            "Start",
            "Setting",
            "67",
            "Exit"
        ]

        # Позиции кнопок (x, y, width, height)
        self.button_rects = []
        self._build_rects()

    def _build_rects(self):
        self.button_rects = []
        y = 220
        for _ in self.options:
            self.button_rects.append(pygame.Rect(270, y - 5, 260, 50))
            y += 60
    # DRAW MENU
    def draw(self, screen, font):
        screen.fill('#71ddee')

        # title
        title = font.render("YERZAT 67", True, (255, 255, 255))
        screen.blit(title, (280, 120))

        mouse_pos = pygame.mouse.get_pos()

        y = 220
        for i, option in enumerate(self.options):
            rect = self.button_rects[i]

            # Подсветка если мышь наведена или выбрано клавишей
            hovered = rect.collidepoint(mouse_pos)

            if i == self.selected_option or hovered:
                color = (255, 255, 0)
                # фон кнопки при наведении
                pygame.draw.rect(screen, (80, 180, 200), rect, border_radius=8)
                pygame.draw.rect(screen, (255, 255, 0), rect, 2, border_radius=8)
            else:
                color = (255, 255, 255)

            text = font.render(option, True, color)
            screen.blit(text, (300, y))
            y += 60

    # MOUSE 
 
    def handle_mouse_motion(self, mouse_pos):
        for i, rect in enumerate(self.button_rects):
            if rect.collidepoint(mouse_pos):
                self.selected_option = i

   

    def handle_mouse_click(self, mouse_pos):
        for i, rect in enumerate(self.button_rects):
            if rect.collidepoint(mouse_pos):
                self.selected_option = i
                return self.select()
        return None

    
    def move_up(self):
        self.selected_option -= 1
        if self.selected_option < 0:
            self.selected_option = len(self.options) - 1

    

    def move_down(self):
        self.selected_option += 1
        if self.selected_option >= len(self.options):
            self.selected_option = 0

   
    def get_selected(self):
        return self.options[self.selected_option]

    

    def select(self):
        option = self.get_selected()
        if option == "Exit":
            pygame.quit()
            quit()
        return option
