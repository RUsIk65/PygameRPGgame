# systems/inventory.py — Инвентарь: хранение, экипировка, вычисление статов

import json
import os
import random

# Загружаем базу данных предметов из JSON при импорте
_DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "items.json")
with open(_DATA_PATH, "r", encoding="utf-8") as f:
    ITEMS_DB = {item["id"]: item for item in json.load(f)}


class Item:
    """Экземпляр предмета в игре."""

    def __init__(self, item_id: str):
        data = ITEMS_DB[item_id]
        self.id       = data["id"]
        self.name     = data["name"]
        self.type     = data["type"]        # weapon / armor / accessory
        self.rarity   = data["rarity"]      # common / rare / epic
        self.stats    = dict(data["stats"]) # {attack, defense, speed, hp}
        self.description = data["description"]

    def __repr__(self):
        return f"<Item {self.name} [{self.rarity}]>"


class Inventory:
    """
    Хранит предметы и отслеживает экипированные слоты.
    Слоты: weapon, armor, accessory.
    """
    MAX_SIZE = 20  # максимум предметов в сумке

    def __init__(self):
        self.items: list[Item] = []          # все предметы
        self.equipped: dict[str, Item | None] = {
            "weapon":    None,
            "armor":     None,
            "accessory": None,
        }

    # ── Основные операции ──────────────────────────────────────────────

    def add_item(self, item: Item) -> bool:
        """Добавить предмет. Возвращает False, если инвентарь полон."""
        if len(self.items) >= self.MAX_SIZE:
            return False
        self.items.append(item)
        return True

    def remove_item(self, item: Item):
        """Удалить предмет (например, при экипировке в слот)."""
        if item in self.items:
            self.items.remove(item)

    def equip(self, item: Item) -> Item | None:
        """
        Экипировать предмет в нужный слот.
        Возвращает ранее экипированный предмет (или None),
        который нужно вернуть в инвентарь.
        """
        slot = item.type
        if slot not in self.equipped:
            return None

        old_item = self.equipped[slot]
        self.equipped[slot] = item
        self.remove_item(item)          # убираем из сумки
        if old_item:
            self.items.append(old_item) # возвращаем старый предмет в сумку
        return old_item

    def unequip(self, slot: str) -> bool:
        """Снять предмет из слота в сумку."""
        item = self.equipped.get(slot)
        if item and len(self.items) < self.MAX_SIZE:
            self.items.append(item)
            self.equipped[slot] = None
            return True
        return False

    # ── Расчёт бонусов ──────────────────────────────────────────────────

    def get_bonus_stats(self) -> dict:
        """Суммировать статы всех экипированных предметов."""
        bonus = {"attack": 0, "defense": 0, "speed": 0, "hp": 0}
        for item in self.equipped.values():
            if item:
                for stat, val in item.stats.items():
                    bonus[stat] += val
        return bonus

    # ── Утилиты ─────────────────────────────────────────────────────────

    def get_item_at_index(self, index: int) -> Item | None:
        if 0 <= index < len(self.items):
            return self.items[index]
        return None

    @property
    def count(self) -> int:
        return len(self.items)
