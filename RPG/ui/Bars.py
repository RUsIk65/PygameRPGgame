import pygame


class Bar:

    def __init__(
        self,
        x,
        y,
        width,
        height,
        max_value,
        color
    ):

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.max_value = max_value

        self.color = color

    def draw(self, screen, current_value):

        # background
        pygame.draw.rect(
            screen,
            (50, 50, 50),
            (
                self.x,
                self.y,
                self.width,
                self.height
            )
        )

        # fill
        fill = max(4, (current_value / self.max_value) * self.width)

        # bar
        pygame.draw.rect(
            screen,
            self.color,
            (
                self.x,
                self.y,
                fill,
                self.height
            )
        )

        # border
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (
                self.x,
                self.y,
                self.width,
                self.height
            ),
            2
        )
