# ui/inventory_ui.py — Экран инвентаря: слоты, экипировка, подсветка редкости

import pygame
from settings import (WHITE, DARK_GREY, YELLOW, RARITY_COLORS,
                      SCREEN_WIDTH, SCREEN_HEIGHT, BLACK)


class InventoryUI:
    """
    Полноэкранный оверлей инвентаря.
    Открывается/закрывается по клавише I.
    Слева — сумка (список предметов).
    Справа — слоты экипировки.
    """

    SLOT_W    = 190
    SLOT_H    = 28
    MARGIN    = 12
    BAG_X     = 60
    BAG_Y     = 80
    EQUIP_X   = SCREEN_WIDTH // 2 + 40
    EQUIP_Y   = 100

    def __init__(self):
        self.visible       = False
        self._selected_idx = 0          # выбранный предмет в сумке
        self._font_title   = pygame.font.SysFont("monospace", 20, bold=True)
        self._font_item    = pygame.font.SysFont("monospace", 14)
        self._font_desc    = pygame.font.SysFont("monospace", 12)

    # ── Управление ──────────────────────────────────────────────────────

    def toggle(self):
        self.visible = not self.visible

    def handle_event(self, event: pygame.event.Event, inventory) -> str | None:
        """
        Обработать ввод.
        Возвращает команду ('equip', 'unequip_weapon', …) или None.
        """
        if not self.visible:
            return None

        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP,   pygame.K_w):
                self._selected_idx = max(0, self._selected_idx - 1)
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                max_idx = max(0, inventory.count - 1)
                self._selected_idx = min(max_idx, self._selected_idx + 1)
            elif event.key == pygame.K_RETURN:
                # Экипировать выбранный предмет
                item = inventory.get_item_at_index(self._selected_idx)
                if item:
                    inventory.equip(item)
                    self._selected_idx = max(0, self._selected_idx - 1)
                    return "equip"
        return None

    # ── Рендер ──────────────────────────────────────────────────────────

    def draw(self, surface: pygame.Surface, inventory, player_stats: dict):
        if not self.visible:
            return

        # Полупрозрачный фон
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((8, 8, 18, 210))
        surface.blit(overlay, (0, 0))

        # Заголовок
        title = self._font_title.render("── ИНВЕНТАРЬ ──", True, YELLOW)
        surface.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 30))

        self._draw_bag(surface, inventory)
        self._draw_equipped(surface, inventory)
        self._draw_total_stats(surface, player_stats)
        self._draw_hint(surface, inventory)

    def _draw_bag(self, surface: pygame.Surface, inventory):
        """Список предметов в сумке."""
        head = self._font_item.render(
            f"Сумка  ({inventory.count}/{inventory.MAX_SIZE})", True, WHITE)
        surface.blit(head, (self.BAG_X, self.BAG_Y - 26))

        for i, item in enumerate(inventory.items):
            y    = self.BAG_Y + i * (self.SLOT_H + 2)
            rect = pygame.Rect(self.BAG_X, y, self.SLOT_W, self.SLOT_H)

            # Фон слота
            bg_col = (40, 60, 90) if i == self._selected_idx else (25, 25, 35)
            pygame.draw.rect(surface, bg_col, rect, border_radius=4)

            # Цвет редкости
            rarity_col = RARITY_COLORS[item.rarity]
            pygame.draw.rect(surface, rarity_col, rect, 2, border_radius=4)

            # Иконка типа
            icon_map = {"weapon": "⚔", "armor": "🛡", "accessory": "💎"}
            icon = icon_map.get(item.type, "?")
            icon_surf = self._font_item.render(icon, True, rarity_col)
            surface.blit(icon_surf, (rect.x + 6, rect.y + 6))

            # Название
            name_surf = self._font_item.render(item.name, True, rarity_col)
            surface.blit(name_surf, (rect.x + 30, rect.y + 6))

        # Описание выбранного предмета
        sel = inventory.get_item_at_index(self._selected_idx)
        if sel:
            desc_y = self.BAG_Y + inventory.MAX_SIZE * (self.SLOT_H + 2) + 10
            desc_y = min(desc_y, SCREEN_HEIGHT - 80)
            desc   = self._font_desc.render(sel.description, True,
                                            (160, 160, 170))
            surface.blit(desc, (self.BAG_X, desc_y))

            # Статы
            stats_txt = (f"+ATK {sel.stats['attack']}  "
                         f"+DEF {sel.stats['defense']}  "
                         f"+SPD {sel.stats['speed']}  "
                         f"+HP {sel.stats['hp']}")
            st_surf = self._font_desc.render(stats_txt, True,
                                             RARITY_COLORS[sel.rarity])
            surface.blit(st_surf, (self.BAG_X, desc_y + 18))

    def _draw_equipped(self, surface: pygame.Surface, inventory):
        """Слоты экипировки справа."""
        head = self._font_item.render("Экипировка", True, WHITE)
        surface.blit(head, (self.EQUIP_X, self.EQUIP_Y - 26))

        slots = [
            ("weapon",    "⚔  Оружие"),
            ("armor",     "🛡  Броня"),
            ("accessory", "💎  Аксессуар"),
        ]
        for i, (slot_key, slot_label) in enumerate(slots):
            y    = self.EQUIP_Y + i * 70
            rect = pygame.Rect(self.EQUIP_X, y, 220, 60)

            item = inventory.equipped.get(slot_key)
            bg   = (30, 40, 60) if item else (20, 20, 28)
            pygame.draw.rect(surface, bg,    rect, border_radius=6)
            pygame.draw.rect(surface, (70, 90, 130), rect, 2, border_radius=6)

            # Метка слота
            lbl = self._font_desc.render(slot_label, True, (120, 140, 160))
            surface.blit(lbl, (rect.x + 8, rect.y + 6))

            if item:
                col      = RARITY_COLORS[item.rarity]
                name_s   = self._font_item.render(item.name, True, col)
                surface.blit(name_s, (rect.x + 8, rect.y + 26))
            else:
                empty_s  = self._font_desc.render("— пусто —", True,
                                                   (70, 70, 80))
                surface.blit(empty_s, (rect.x + 8, rect.y + 26))

    def _draw_total_stats(self, surface: pygame.Surface, stats: dict):
        """Итоговые статы персонажа."""
        x, y = self.EQUIP_X, self.EQUIP_Y + 3 * 70 + 20
        head = self._font_item.render("Итоговые статы", True, WHITE)
        surface.blit(head, (x, y))
        lines = [
            ("HP",      stats.get("hp",      0),  GREEN   := (50, 200, 80)),
            ("Атака",   stats.get("attack",  0),  (255, 100, 100)),
            ("Защита",  stats.get("defense", 0),  (100, 160, 255)),
            ("Скорость",stats.get("speed",   0),  (255, 220, 60)),
        ]
        for j, (name, val, col) in enumerate(lines):
            row = self._font_desc.render(f"{name}: {val}", True, col)
            surface.blit(row, (x, y + 20 + j * 16))

    def _draw_hint(self, surface: pygame.Surface, inventory):
        """Подсказка управления."""
        hints = "↑↓ — выбор   Enter — экипировать   I — закрыть"
        h_surf = self._font_desc.render(hints, True, (100, 100, 120))
        surface.blit(h_surf,
                     (SCREEN_WIDTH // 2 - h_surf.get_width() // 2,
                      SCREEN_HEIGHT - 24))
