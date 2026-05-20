# ui/hud.py — HUD: HP-бар, статы игрока, уведомления

import pygame
from settings import (SCREEN_WIDTH, SCREEN_HEIGHT, RED, GREEN,
                      WHITE, DARK_GREY, YELLOW, RARITY_COLORS,
                      ATTACK_COOLDOWN)
import time


class Notification:
    """Всплывающее сообщение в углу экрана."""

    def __init__(self, text: str, color: tuple, duration: float = 2.5):
        self.text     = text
        self.color    = color
        self.duration = duration
        self.timer    = duration

    @property
    def alive(self) -> bool:
        return self.timer > 0


class HUD:
    """
    Рисует поверх игрового мира:
    – HP-бар игрока
    – Текущие статы (attack, defense, speed)
    – Подсказки управления
    – Очередь уведомлений
    """

    def __init__(self):
        self._font_large  = pygame.font.SysFont("monospace", 20, bold=True)
        self._font_medium = pygame.font.SysFont("monospace", 15)
        self._font_small  = pygame.font.SysFont("monospace", 12)
        self._notifications: list[Notification] = []
        self._attack_flash  = 0.0  # секунды подсветки кнопки атаки

    # ── Обновление ──────────────────────────────────────────────────────

    def update(self, dt: float):
        for n in self._notifications:
            n.timer -= dt
        self._notifications = [n for n in self._notifications if n.alive]
        if self._attack_flash > 0:
            self._attack_flash -= dt

    def notify(self, text: str, color: tuple = WHITE, duration: float = 2.5):
        """Добавить уведомление (максимум 4 одновременно)."""
        self._notifications = self._notifications[-3:]
        self._notifications.append(Notification(text, color, duration))

    def flash_attack(self):
        self._attack_flash = 0.3

    # ── Рендер ──────────────────────────────────────────────────────────

    def draw(self, surface: pygame.Surface, player):
        self._draw_hp_bar(surface, player)
        self._draw_stats_panel(surface, player)
        self._draw_hints(surface)
        self._draw_notifications(surface)

    def _draw_hp_bar(self, surface: pygame.Surface, player):
        """Большой HP-бар внизу слева."""
        BAR_X, BAR_Y = 16, SCREEN_HEIGHT - 48
        BAR_W, BAR_H = 240, 22
        ratio = max(0.0, player.hp / player.max_hp)

        # Фон
        pygame.draw.rect(surface, (40, 10, 10),
                         (BAR_X, BAR_Y, BAR_W, BAR_H), border_radius=4)
        # Заполнение
        fill_color = GREEN if ratio > 0.5 else (YELLOW if ratio > 0.25 else RED)
        pygame.draw.rect(surface, fill_color,
                         (BAR_X, BAR_Y, int(BAR_W * ratio), BAR_H),
                         border_radius=4)
        # Рамка
        pygame.draw.rect(surface, WHITE,
                         (BAR_X, BAR_Y, BAR_W, BAR_H), 2, border_radius=4)

        # Текст HP
        txt = self._font_medium.render(
            f"HP  {player.hp} / {player.max_hp}", True, WHITE)
        surface.blit(txt, (BAR_X + 8, BAR_Y + 3))

    def _draw_stats_panel(self, surface: pygame.Surface, player):
        """Маленькая панель статов."""
        stats  = player.effective_stats
        PANEL_X, PANEL_Y = 16, SCREEN_HEIGHT - 100
        lines  = [
            f"ATK  {stats['attack']}",
            f"DEF  {stats['defense']}",
            f"SPD  {stats['speed']}",
        ]
        for i, line in enumerate(lines):
            txt = self._font_small.render(line, True, (180, 200, 220))
            surface.blit(txt, (PANEL_X, PANEL_Y + i * 16))

    def _draw_hints(self, surface: pygame.Surface):
        """Подсказки управления внизу справа."""
        hints = [
            ("WASD",    "Движение"),
            ("J / LMB", "Атака"),
            ("E",       "Взаимодействие"),
            ("I",       "Инвентарь"),
            ("F",       "Подобрать"),
        ]
        x = SCREEN_WIDTH - 180
        y = SCREEN_HEIGHT - 16 - len(hints) * 16

        for key, desc in hints:
            key_surf  = self._font_small.render(key,  True, YELLOW)
            desc_surf = self._font_small.render(f" — {desc}", True,
                                                (160, 160, 170))
            surface.blit(key_surf,  (x, y))
            surface.blit(desc_surf, (x + key_surf.get_width(), y))
            y += 16

    def _draw_notifications(self, surface: pygame.Surface):
        """Стек уведомлений справа сверху."""
        x = SCREEN_WIDTH - 280
        y = 12
        for n in reversed(self._notifications):
            alpha = int(255 * min(1.0, n.timer / 0.5))
            txt   = self._font_medium.render(n.text, True, n.color)
            txt.set_alpha(alpha)
            surface.blit(txt, (x, y))
            y += 22
