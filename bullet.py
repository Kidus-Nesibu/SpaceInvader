# bullet.py
import pygame
from settings import RED

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.y -= 15  # Increased speed
        if self.rect.bottom < 0:
            self.kill()
