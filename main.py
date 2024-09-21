# main.py
import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BLUE_BLACK, FPS, ALIEN_PATHS
from player import Player
from bullet import Bullet
from alien import Alien
from utils import show_game_over

def main_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Space Shooter - Faster Edition')
    clock = pygame.time.Clock()

    player = Player()
    player_group = pygame.sprite.GroupSingle(player)
    bullets = pygame.sprite.Group()
    aliens = pygame.sprite.Group()

    score = 0
    alien_speed = 2  # Increased base speed
    max_aliens_on_screen = 5
    alien_spawn_delay = 800  # Reduced spawn delay
    last_alien_spawn_time = pygame.time.get_ticks()

    shooting = False
    bullet_delay = 150  # Reduced delay between bullets
    last_bullet_time = pygame.time.get_ticks()

    running = True

    while running:
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shooting = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    shooting = False

        # Player Movement
        player_group.update()

        # Bullet Firing
        if shooting:
            current_time = pygame.time.get_ticks()
            if current_time - last_bullet_time > bullet_delay:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                bullets.add(bullet)
                last_bullet_time = current_time

        # Bullet Movement
        bullets.update()

        # Alien Spawning
        current_time = pygame.time.get_ticks()
        if current_time - last_alien_spawn_time > alien_spawn_delay and len(aliens) < max_aliens_on_screen:
            alien_type = min(score // 100, 4)  # Based on score, introduce new alien types
            alien = Alien(ALIEN_PATHS[alien_type], alien_speed)
            aliens.add(alien)
            last_alien_spawn_time = current_time

        # Alien Movement
        aliens.update()

        # Collision Detection
        for bullet in bullets:
            hit_aliens = pygame.sprite.spritecollide(bullet, aliens, True)
            if hit_aliens:
                score += len(hit_aliens)
                bullet.kill()

        # Check Game Over Condition
        for alien in aliens:
            if alien.rect.top >= SCREEN_HEIGHT:
                show_game_over(screen, score)
                return  # Game over, exit the game loop

        # Increase difficulty (speed and max aliens)
        if score > 0 and score % 100 == 0:  # Faster increase in difficulty
            alien_speed += 0.5
            max_aliens_on_screen += 1

        # Clear screen
        screen.fill(BLUE_BLACK)

        # Draw everything
        player_group.draw(screen)
        bullets.draw(screen)
        aliens.draw(screen)

        # Display Score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(score_text, (10, 10))

        # Update display
        pygame.display.flip()

        # Frame Rate
        clock.tick(FPS)

if __name__ == '__main__':
    main_game()
