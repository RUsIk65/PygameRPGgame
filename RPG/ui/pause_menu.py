import pygame


class PauseMenu:

    def __init__(self):
        self.visible = False
        self.options = ["Продолжить", "Сохранить", "Выход"]
        self.selected = 0

        self._font_title = pygame.font.SysFont("Arial", 26, bold=True)
        self._font_item  = pygame.font.SysFont("Arial", 20)
        self._font_hint  = pygame.font.SysFont("Arial", 13)

        self._button_rects = []

    def toggle(self):
        self.visible = not self.visible
        self.selected = 0

    def _build_rects(self, sw, sh):
        self._button_rects = []
        for i in range(len(self.options)):
            y = sh // 2 - 30 + i * 60
            self._button_rects.append(pygame.Rect(sw // 2 - 130, y, 260, 45))

    def handle_event(self, event, sw, sh):
        """
        Возвращает: 'resume', 'save', 'quit' или None
        """
        if not self.visible:
            return None

        self._build_rects(sw, sh)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.visible = False
                return "resume"
            if event.key in (pygame.K_UP, pygame.K_w):
                self.selected = max(0, self.selected - 1)
            if event.key in (pygame.K_DOWN, pygame.K_s):
                self.selected = min(len(self.options) - 1, self.selected + 1)
            if event.key == pygame.K_RETURN:
                return self._action(self.selected)

        if event.type == pygame.MOUSEMOTION:
            for i, rect in enumerate(self._button_rects):
                if rect.collidepoint(event.pos):
                    self.selected = i

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, rect in enumerate(self._button_rects):
                if rect.collidepoint(event.pos):
                    return self._action(i)

        return None

    def _action(self, index):
        label = self.options[index]
        if label == "Продолжить":
            self.visible = False
            return "resume"
        elif label == "Сохранить":
            return "save"
        elif label == "Выход":
            return "quit"
        return None

    def draw(self, surface):
        if not self.visible:
            return

        sw, sh = surface.get_size()
        self._build_rects(sw, sh)

        # Полупрозрачный фон
        overlay = pygame.Surface((sw, sh), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 170))
        surface.blit(overlay, (0, 0))

        # Панель
        panel = pygame.Rect(sw // 2 - 160, sh // 2 - 90, 320, 240)
        pygame.draw.rect(surface, (18, 22, 32), panel, border_radius=10)
        pygame.draw.rect(surface, (80, 100, 140), panel, 2, border_radius=10)

        # Заголовок
        title = self._font_title.render("ПАУЗА", True, (255, 210, 60))
        surface.blit(title, (sw // 2 - title.get_width() // 2, sh // 2 - 80))

        # Кнопки
        for i, (label, rect) in enumerate(zip(self.options, self._button_rects)):
            selected = i == self.selected

            bg  = (50, 70, 110) if selected else (25, 30, 45)
            col = (255, 255, 255) if selected else (160, 160, 170)

            pygame.draw.rect(surface, bg, rect, border_radius=6)
            pygame.draw.rect(surface, (80, 100, 140), rect, 2, border_radius=6)

            text = self._font_item.render(label, True, col)
            surface.blit(text, (
                rect.x + rect.width // 2 - text.get_width() // 2,
                rect.y + rect.height // 2 - text.get_height() // 2
            ))

        # Подсказка
        hint = self._font_hint.render("ESC -- продолжить", True, (80, 80, 100))
        surface.blit(hint, (sw // 2 - hint.get_width() // 2, sh // 2 + 155))