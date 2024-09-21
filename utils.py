# utils.py
import pygame
from settings import WHITE, SCREEN_WIDTH, SCREEN_HEIGHT

def show_game_over(screen, score):
    font = pygame.font.Font(None, 74)
    text = font.render('GAME OVER', True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
    pygame.display.flip()
    pygame.time.wait(2000)
