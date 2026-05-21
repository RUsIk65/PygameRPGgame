import pygame

WHITE      = (255, 255, 255)
YELLOW     = (255, 210, 60)
LIGHT_GREY = (160, 160, 170)
PURPLE     = (160, 60, 220)
BLUE       = (50, 100, 220)
GREEN      = (50, 200, 80)

RARITY_COLORS = {
    "common":    LIGHT_GREY,
    "uncommon":  GREEN,
    "rare":      BLUE,
    "epic":      PURPLE,
    "legendary": (255, 140, 0),
}

ITEM_TYPE_LABEL = {
    "Weapon":   "[W]",
    "Armor":    "[A]",
    "Potion":   "[P]",
    "Food":     "[F]",
    "Backpack": "[B]",
}


class InventoryUI:

    SLOT_W  = 220
    SLOT_H  = 30
    BAG_X   = 60
    BAG_Y   = 100
    EQUIP_X = 520
    EQUIP_Y = 110

    def __init__(self, inventory):
        self.inventory     = inventory
        self.visible       = False
        self._selected_idx = 0

        self._font_title = pygame.font.SysFont("Arial", 20, bold=True)
        self._font_item  = pygame.font.SysFont("Arial", 15)
        self._font_desc  = pygame.font.SysFont("Arial", 13)

    def toggle(self):
        self.visible = not self.visible

    def handle_event(self, event):
        if not self.visible:
            return

        if event.type == pygame.KEYDOWN:
            items = [s for s in self.inventory.slots if s is not None]

            if event.key in (pygame.K_UP, pygame.K_w):
                self._selected_idx = max(0, self._selected_idx - 1)

            elif event.key in (pygame.K_DOWN, pygame.K_s):
                self._selected_idx = min(max(0, len(items) - 1),
                                         self._selected_idx + 1)

            elif event.key == pygame.K_RETURN:
                if items and self._selected_idx < len(items):
                    self._equip_item(items[self._selected_idx])

    def _equip_item(self, item):
        item_type = item.item_type()
        slot = None
        if item_type == "Weapon":
            slot = "weapon"
        elif item_type == "Armor":
            slot = "armor"
        if slot:
            old = self.inventory.equipped.get(slot)
            self.inventory.equipped[slot] = item
            for i, s in enumerate(self.inventory.slots):
                if s is item:
                    self.inventory.slots[i] = old
                    break

    # ── Рендер ──────────────────────────────────────────────────────────

    def draw(self, surface, player=None, font=None):
        if not self.visible:
            return

        sw, sh = surface.get_size()

        overlay = pygame.Surface((sw, sh), pygame.SRCALPHA)
        overlay.fill((8, 8, 18, 215))
        surface.blit(overlay, (0, 0))

        title = self._font_title.render("=== ИНВЕНТАРЬ ===", True, YELLOW)
        surface.blit(title, (sw // 2 - title.get_width() // 2, 35))

        self._draw_bag(surface)
        self._draw_equipped(surface)
        if player:
            self._draw_stats(surface, player)
        self._draw_hint(surface, sw, sh)

    def _draw_bag(self, surface):
        items = [s for s in self.inventory.slots if s is not None]
        count = len(items)
        total = len(self.inventory.slots)

        head = self._font_item.render(f"Сумка  ({count}/{total})", True, WHITE)
        surface.blit(head, (self.BAG_X, self.BAG_Y - 28))

        for i, item in enumerate(items):
            y    = self.BAG_Y + i * (self.SLOT_H + 3)
            rect = pygame.Rect(self.BAG_X, y, self.SLOT_W, self.SLOT_H)

            bg = (40, 60, 90) if i == self._selected_idx else (25, 25, 35)
            pygame.draw.rect(surface, bg, rect, border_radius=4)

            rarity_col = RARITY_COLORS.get(
                getattr(item, "rareness", "common"), LIGHT_GREY)
            pygame.draw.rect(surface, rarity_col, rect, 2, border_radius=4)

            label_s = self._font_desc.render(
                ITEM_TYPE_LABEL.get(item.item_type(), "?"), True, rarity_col)
            surface.blit(label_s, (rect.x + 6, rect.y + 7))

            name_s = self._font_item.render(item.name, True, rarity_col)
            surface.blit(name_s, (rect.x + 34, rect.y + 7))

            stat_str = self._item_stat_str(item)
            if stat_str:
                st_s = self._font_desc.render(stat_str, True, (180, 180, 180))
                surface.blit(st_s, (
                    rect.x + self.SLOT_W - st_s.get_width() - 6,
                    rect.y + 9))

        if items and self._selected_idx < len(items):
            sel = items[self._selected_idx]
            desc_y = self.BAG_Y + len(items) * (self.SLOT_H + 3) + 14
            desc_s = self._font_desc.render(
                getattr(sel, "description", ""), True, (160, 160, 170))
            surface.blit(desc_s, (self.BAG_X, desc_y))

    def _draw_equipped(self, surface):
        head = self._font_item.render("Экипировка", True, WHITE)
        surface.blit(head, (self.EQUIP_X, self.EQUIP_Y - 28))

        slots = [
            ("weapon", "[W] Оружие"),
            ("armor",  "[A] Броня"),
        ]
        for i, (slot_key, slot_label) in enumerate(slots):
            y    = self.EQUIP_Y + i * 80
            rect = pygame.Rect(self.EQUIP_X, y, 260, 70)

            item = self.inventory.equipped.get(slot_key)
            bg   = (30, 40, 60) if item else (20, 20, 28)
            pygame.draw.rect(surface, bg, rect, border_radius=6)
            pygame.draw.rect(surface, (70, 90, 130), rect, 2, border_radius=6)

            lbl = self._font_desc.render(slot_label, True, (120, 140, 160))
            surface.blit(lbl, (rect.x + 8, rect.y + 8))

            if item:
                col    = RARITY_COLORS.get(
                    getattr(item, "rareness", "common"), LIGHT_GREY)
                name_s = self._font_item.render(item.name, True, col)
                surface.blit(name_s, (rect.x + 8, rect.y + 28))
                stat_s = self._font_desc.render(
                    self._item_stat_str(item), True, (180, 180, 180))
                surface.blit(stat_s, (rect.x + 8, rect.y + 50))
            else:
                empty_s = self._font_desc.render(
                    "-- пусто --", True, (70, 70, 80))
                surface.blit(empty_s, (rect.x + 8, rect.y + 28))

    def _draw_stats(self, surface, player):
        x = self.EQUIP_X
        y = self.EQUIP_Y + 2 * 80 + 20

        # Фон блока статов
        rect = pygame.Rect(x, y, 260, 140)
        pygame.draw.rect(surface, (18, 22, 32), rect, border_radius=6)
        pygame.draw.rect(surface, (70, 90, 130), rect, 2, border_radius=6)

        head = self._font_item.render("Итоговые статы", True, WHITE)
        surface.blit(head, (x + 8, y + 8))

        # Бонус от экипировки
        bonus_atk = 0
        bonus_def = 0
        w = self.inventory.equipped.get("weapon")
        a = self.inventory.equipped.get("armor")
        if w:
            bonus_atk += getattr(w, "damage", 0)
        if a:
            bonus_def += getattr(a, "defense", 0)

        lines = [
            (f"HP:      {player.current_hp} / {player.max_hp}",    (255, 100, 100)),
            (f"Mana:    {player.current_mana} / {player.max_mana}", (100, 160, 255)),
            (f"Атака:   {player._attack} (+{bonus_atk})",           (255, 200, 80)),
            (f"Защита:  {player._defense} (+{bonus_def})",          (100, 220, 255)),
            (f"Скорость:{player._speed}",                           (180, 255, 180)),
            (f"Крит:    {player._crit_chance}%",                    (255, 160, 60)),
        ]

        for i, (text, color) in enumerate(lines):
            s = self._font_desc.render(text, True, color)
            surface.blit(s, (x + 10, y + 30 + i * 18))

    def _item_stat_str(self, item):
        t = item.item_type()
        if t == "Weapon":
            return f"DMG +{item.damage}"
        elif t == "Armor":
            return f"DEF +{item.defense}"
        elif t == "Potion":
            return f"MP +{item.mana_restore}"
        elif t == "Food":
            return f"HP +{item.health_restore}"
        return ""

    def _draw_hint(self, surface, sw, sh):
        hints = "Стрелки -- выбор   Enter -- экипировать   I -- закрыть"
        h_s = self._font_desc.render(hints, True, (100, 100, 120))
        surface.blit(h_s, (sw // 2 - h_s.get_width() // 2, sh - 26))
