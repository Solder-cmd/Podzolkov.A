import pygame
from random import randint, choice

class Coin:
    def __init__(self, x, y):
        self.radius = 10
        self.x = x
        self.y = y
        self.color = "gold"
        self.speed = 3
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


class Enemy:
    def __init__(self, x, y):
        self.width = 50
        self.height = 30
        self.rect = pygame.rect.Rect(x, y, self.width, self.height)
        self.health = randint(1, 3)

    def draw(self, screen):
        color = None
        if self.health == 3:
            color = "green"
        elif self.health == 2:
            color = "yellow"
        else:
            color = 'red'
        pygame.draw.rect(screen, color, self.rect)

    def check_collision(self, ball):
        if self.rect.colliderect(ball.rect):
            self.health -= 1
            if self.health <= 0:
                return True  # Убит
        return False
