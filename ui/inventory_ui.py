import pygame


class InventoryUI:

    def __init__(self, inventory):

        self.inventory = inventory

        self.cols = 8
        self.slot_size = 50
        self.margin = 10

        self.start_x = 150
        self.start_y = 180

    # DRAW INVENTORY

    def draw(self, screen, font):

        # background
        pygame.draw.rect(
            screen,
            (25, 25, 25),
            (100, 100, 600, 350)
        )

        # border
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (100, 100, 600, 350),
            3
        )

        # title
        title = font.render(
            "INVENTORY",
            True,
            (255, 255, 255)
        )

        screen.blit(title, (300, 120))

        # slots
        for i, item in enumerate(self.inventory.slots):

            row = i // self.cols
            col = i % self.cols

            x = self.start_x + col * (self.slot_size + self.margin)
            y = self.start_y + row * (self.slot_size + self.margin)

            # slot background
            pygame.draw.rect(
                screen,
                (70, 70, 70),
                (x, y, self.slot_size, self.slot_size)
            )

            # slot border
            pygame.draw.rect(
                screen,
                (255, 255, 255),
                (x, y, self.slot_size, self.slot_size),
                2
            )

            # item text
            if item:

                text = font.render(
                    item.name[:2],
                    True,
                    (255, 255, 0)
                )

                screen.blit(text, (x + 10, y + 10))
