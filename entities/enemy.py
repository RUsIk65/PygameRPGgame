import pygame, math
from BaseEntity import BaseEntity
from systems.stats import Stats

class Enemy(BaseEntity, Stats):
    def __init__(self, id, name, image, pos,
            hp = 100, mana = 50, attack = 20,
            defense = 10, speed = 10, attack_range=0,
            crit_chance=0, level = 1
            ):

        BaseEntity.__init__(self, id, name, image, pos)
        Stats.__init__(self, hp, mana, attack, defense,
                       speed, attack_range, crit_chance, level)

        self._state = "idle"   # idle | chase | attack
        self._patrol_timer = 0.0
        self._patrol_dir = (0.0, 0.0)

        self.last_attack_time = 0.0
        self.attack_cooldown = 1.2

        self.dead = False

    def take_damage(self, amount: int):
        self.hp = max(0, self.hp - amount)
        self._hit_flash = 0.2
        if self.hp <= 0:
            self.dead = True

    @property
    def alive(self) -> bool:
        return not self.dead


    def entity_type(self):
        return "Enemy"

    def entity_info(self):
        return (f"ID: {self.id}"
        f"Name: {self.name}"
        f"HP: {self.hp}"
        f"Defense: {self.defense}"
        f"Attack: {self.attack}"
        f"Speed: {self.speed}"
        f"Radar Range: {self.radar_range}"
        f"Image: {self.image}")

    def update(self, dt: float, player_x: float, player_y: float,
               wall_rects: list[pygame.Rect]):
        if self.dead:
            return

        dist = math.hypot(player_x - self.x, player_y - self.y)

        # Переходы состояний
        if dist < 200:
            self._state = "chase"
        else:
            self._state = "idle"

        if self._state == "chase":
            self._chase(dt, player_x, player_y, wall_rects)
        else:
            self._patrol(dt, wall_rects)

        # Хит-флаш
        if self._hit_flash > 0:
            self._hit_flash -= dt

    def _chase(self, dt: float, tx: float, ty: float,
               walls: list[pygame.Rect]):
        """Двигаться к цели."""
        dx = tx - self.x
        dy = ty - self.y
        dist = math.hypot(dx, dy)
        if dist < 1:
            return

        speed = self.stats["speed"]
        nx    = dx / dist * speed * dt
        ny    = dy / dist * speed * dt

        self._move_with_collision(nx, 0,  walls)
        self._move_with_collision(0,  ny, walls)

    def _patrol(self, dt: float, walls: list[pygame.Rect]):
        """Случайное блуждание."""
        import random
        self._patrol_timer -= dt
        if self._patrol_timer <= 0:
            self._patrol_timer = random.uniform(1.0, 3.0)
            angle = random.uniform(0, 2 * math.pi)
            self._patrol_dir  = (math.cos(angle), math.sin(angle))

        spd  = self.stats["speed"] * 0.4 * dt
        self._move_with_collision(self._patrol_dir[0] * spd, 0,  walls)
        self._move_with_collision(0, self._patrol_dir[1] * spd, walls)

    def _move_with_collision(self, dx: float, dy: float,
                              walls: list[pygame.Rect]):
        self.x += dx
        self.y += dy
        r = self._get_rect()
        for wall in walls:
            if r.colliderect(wall):
                self.x -= dx
                self.y -= dy
                # При столкновении сбросить patrol-направление
                self._patrol_dir = (0.0, 0.0)
                return

    def _get_rect(self) -> pygame.Rect:
        s = self.SIZE
        return pygame.Rect(self.x - s//2, self.y - s//2, s, s)
