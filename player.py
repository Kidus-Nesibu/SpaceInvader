# player.py
import pygame
from settings import SCREEN_WIDTH, SPACESHIP_PATH

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(SPACESHIP_PATH)
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, 550))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= 8  # Increased speed
        if keys[pygame.K_RIGHT] and self.rect.x < SCREEN_WIDTH - self.rect.width:
            self.rect.x += 8  # Increased speed
