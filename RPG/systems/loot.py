# systems/loot.py — Генератор лута с системой редкости

import random
from systems.inventory import Item, ITEMS_DB

# Шансы редкости при дропе (в процентах)
RARITY_WEIGHTS = {
    "common": 40,
    "rare":   20,
    "epic":   7,
}

# Группируем предметы по редкости для быстрого выбора
_BY_RARITY: dict[str, list[str]] = {"common": [], "rare": [], "epic": []}
for _id, _data in ITEMS_DB.items():
    _BY_RARITY[_data["rarity"]].append(_id)


class DroppedItem:
    """Предмет, лежащий на земле (с позицией на карте)."""

    def __init__(self, item: Item, x: float, y: float):
        self.item = item
        self.x    = x
        self.y    = y

    @property
    def rect(self):
        import pygame
        return pygame.Rect(self.x - 8, self.y - 8, 16, 16)


class LootSystem:
    """
    Управляет генерацией и хранением выпавшего лута.
    dropped_items — список DroppedItem на карте.
    """

    def __init__(self):
        self.dropped_items: list[DroppedItem] = []

    def drop_loot(self, x: float, y: float, drop_count: int = 1):
        """
        Сгенерировать drop_count предметов около (x, y).
        С вероятностью ~70% враг что-то дропает.
        """
        for _ in range(drop_count):
            if random.random() > 0.70:   # 30% шанс не дропнуть ничего
                continue

            rarity = self._roll_rarity()
            candidates = _BY_RARITY.get(rarity, [])
            if not candidates:
                continue

            item_id = random.choice(candidates)
            item    = Item(item_id)

            # Небольшой разброс позиции
            dx = random.uniform(-18, 18)
            dy = random.uniform(-18, 18)
            self.dropped_items.append(DroppedItem(item, x + dx, y + dy))

    def _roll_rarity(self) -> str:
        """Выбрать редкость по весам."""
        rarities = list(RARITY_WEIGHTS.keys())
        weights  = list(RARITY_WEIGHTS.values())
        return random.choices(rarities, weights=weights, k=1)[0]

    def try_pickup(self, player_x: float, player_y: float,
                   pickup_range: float) -> DroppedItem | None:
        """
        Проверить, есть ли предмет в радиусе pickup_range.
        Возвращает ближайший DroppedItem или None.
        """
        best     = None
        best_dist = pickup_range

        for di in self.dropped_items:
            dist = ((di.x - player_x) ** 2 + (di.y - player_y) ** 2) ** 0.5
            if dist < best_dist:
                best_dist = dist
                best      = di

        if best:
            self.dropped_items.remove(best)
        return best

    def draw(self, surface, camera_offset_x: float, camera_offset_y: float):
        """Отрисовать все предметы на земле с анимацией мерцания."""
        RARITY_COLORS = {
            "common": (160, 160, 170),
            "rare":   (50,  100, 220),
            "epic":   (160, 60,  220),
        }
        import pygame
        for di in self.dropped_items:
            sx = di.x - camera_offset_x
            sy = di.y - camera_offset_y

            # Пропускаем невидимые предметы
            if not (-20 < sx < surface.get_width() + 20):
                continue
            if not (-20 < sy < surface.get_height() + 20):
                continue

            color = RARITY_COLORS[di.item.rarity]

            # Внешнее свечение (размытый круг)
            glow_surf = pygame.Surface((24, 24), pygame.SRCALPHA)
            pygame.draw.circle(glow_surf, (*color, 60), (12, 12), 12)
            surface.blit(glow_surf, (sx - 12, sy - 12))

            # Ромбик предмета
            points = [
                (sx,      sy - 8),
                (sx + 7,  sy),
                (sx,      sy + 8),
                (sx - 7,  sy),
            ]
            pygame.draw.polygon(surface, color, points)
            pygame.draw.polygon(surface, (255, 255, 255), points, 1)
