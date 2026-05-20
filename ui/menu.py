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

    # =========================
    # DRAW MENU
    # =========================

    def draw(self, screen, font):

        screen.fill('#71ddee')

        # title
        title = font.render("YERZAT 67", True, (255, 255, 255))
        screen.blit(title, (280, 120))

        y = 220

        for i, option in enumerate(self.options):

            if i == self.selected_option:
                color = (255, 255, 0)
            else:
                color = (255, 255, 255)

            text = font.render(option, True, color)
            screen.blit(text, (300, y))

            y += 60

    # =========================
    # MOVE UP
    # =========================

    def move_up(self):

        self.selected_option -= 1

        if self.selected_option < 0:
            self.selected_option = len(self.options) - 1

    # =========================
    # MOVE DOWN
    # =========================

    def move_down(self):

        self.selected_option += 1

        if self.selected_option >= len(self.options):
            self.selected_option = 0

    # =========================
    # GET SELECTED OPTION
    # =========================

    def get_selected(self):

        return self.options[self.selected_option]

    # =========================
    # ACTIONS
    # =========================

    def select(self):

        option = self.get_selected()

        if option == "Exit":
            pygame.quit()
            quit()

        # остальные кнопки просто возвращают действие
        return option
