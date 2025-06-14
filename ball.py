import random

import pygame


class Ball:
    def __init__(self, pos):
        self.size = 50
        self.rect = pygame.Rect(0, 0, self.size, self.size)
        self.rect.center = pos
        self.color = "pink"
        self.dx = 3
        self.dy = -3

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.size / 2)

    def move(self, screen, platform):
        self.rect.x += self.dx
        self.rect.y += self.dy

        width, height = screen.get_size()
        if self.rect.right >= width:
            self.dx = -3
        elif self.rect.x <= 0:
            self.dx = 3
        if self.rect.y <= 0:
            self.dy = 3

        if self.rect.colliderect(platform.rect):
            self.dy = -3
            self.dx = random.choice([-3, 3])

    def reflect(self, enemy):
        # Определим перекрытие по X и Y
        dx = min(self.rect.right - enemy.rect.left, enemy.rect.right - self.rect.left)
        dy = min(self.rect.bottom - enemy.rect.top, enemy.rect.bottom - self.rect.top)

        # Отражаем по направлению наименьшего проникновения
        if dx < dy:
            # Отражение по горизонтали
            self.dx *= -1
            if self.rect.centerx < enemy.rect.centerx:
                self.rect.right = enemy.rect.left  # корректируем позицию
            else:
                self.rect.left = enemy.rect.right
        else:
            # Отражение по вертикали
            self.dy *= -1
            if self.rect.centery < enemy.rect.centery:
                self.rect.bottom = enemy.rect.top
            else:
                self.rect.top = enemy.rect.bottom
