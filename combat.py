# systems/combat.py — Боевая система: атаки, урон, кулдауны

import time
import math
from settings import ATTACK_RANGE, ATTACK_COOLDOWN


class CombatSystem:
    """
    Обрабатывает атаки игрока и врагов.
    Хранит визуальные эффекты удара.
    """

    def __init__(self):
        self._last_player_attack = 0.0   # timestamp последней атаки игрока
        self.hit_effects: list[dict] = []  # [{x, y, timer, color}]

    # ── Атака игрока ────────────────────────────────────────────────────

    def player_attack(self, player, enemies: list) -> list:
        """
        Попытка атаковать ближайших врагов.
        Возвращает список врагов, которым нанесён урон.
        """
        now = time.time()
        if now - self._last_player_attack < ATTACK_COOLDOWN:
            return []

        self._last_player_attack = now
        hit_enemies = []

        for enemy in enemies:
            dist = math.hypot(enemy.x - player.x, enemy.y - player.y)
            if dist <= ATTACK_RANGE:
                damage = self._calc_damage(
                    player.effective_stats["attack"],
                    enemy.stats["defense"]
                )
                enemy.take_damage(damage)
                hit_enemies.append(enemy)

                # Визуальный эффект удара
                self.hit_effects.append({
                    "x":     enemy.x,
                    "y":     enemy.y - 20,
                    "text":  str(damage),
                    "timer": 0.8,
                    "color": (255, 80, 80),
                })

        return hit_enemies

    # ── Атака врага на игрока ────────────────────────────────────────────

    def enemy_attack(self, enemy, player) -> int:
        """Враг атакует игрока. Возвращает нанесённый урон (0 если кулдаун)."""
        now = time.time()
        if now - enemy.last_attack_time < enemy.attack_cooldown:
            return 0

        enemy.last_attack_time = now
        damage = self._calc_damage(
            enemy.stats["attack"],
            player.effective_stats["defense"]
        )
        player.take_damage(damage)

        # Эффект урона по игроку
        self.hit_effects.append({
            "x":     player.x,
            "y":     player.y - 20,
            "text":  str(damage),
            "timer": 0.8,
            "color": (255, 200, 50),
        })
        return damage

    # ── Обновление эффектов ─────────────────────────────────────────────

    def update(self, dt: float):
        """Уменьшаем таймеры визуальных эффектов."""
        for fx in self.hit_effects:
            fx["timer"] -= dt
            fx["y"]     -= 20 * dt   # число «всплывает» вверх
        self.hit_effects = [fx for fx in self.hit_effects if fx["timer"] > 0]

    # ── Рендер эффектов ─────────────────────────────────────────────────

    def draw(self, surface, cam_x: float, cam_y: float):
        """Отрисовать всплывающие числа урона."""
        import pygame
        font = pygame.font.SysFont("monospace", 16, bold=True)

        for fx in self.hit_effects:
            alpha = int(255 * (fx["timer"] / 0.8))
            color = fx["color"]
            text_surf = font.render(fx["text"], True, color)
            text_surf.set_alpha(alpha)
            sx = fx["x"] - cam_x - text_surf.get_width() // 2
            sy = fx["y"] - cam_y
            surface.blit(text_surf, (sx, sy))

    # ── Вспомогательное ─────────────────────────────────────────────────

    @staticmethod
    def _calc_damage(attack: int, defense: int) -> int:
        """Формула урона: минимум 1."""
        import random
        # небольшая вариативность ±20%
        base   = max(1, attack - defense)
        spread = max(1, int(base * 0.2))
        return base + random.randint(-spread, spread)

    @property
    def player_can_attack(self) -> bool:
        return time.time() - self._last_player_attack >= ATTACK_COOLDOWN
