import pygame
import random

#initialize the pygame
pygame.init()

# creates the screen
screen = pygame.display.set_mode((800,600))

#Background
background = pygame.image.load('background.png')

# Title
pygame.display.set_caption("SpaceInvaders")

# Icon
icon = pygame.image.load('ufo.png')
#pygame.display.set_icon(icon)

#player
playerimg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

#Enemey
enemeyimg = pygame.image.load('enemy.png')
enemeyX = random.randint(0, 800)
enemeyY = random.randint(50, 150)
enemeyX_change = 3
enemeyY_change = 40

#Bullet
bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

def player(x, y):
    # blit means draw
    screen.blit(playerimg,(x, y))
def enemey(x, y):
    screen.blit(enemeyimg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))

#Game loop
running = True
while running:
    for event in pygame.event.get(): # this method gives me the event that are happening in the pygame window
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed checks whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 5
            elif event.key == pygame.K_RIGHT:
                playerX_change += 5
            elif event.key == pygame.K_SPACE:
                fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    #this function accepts rgb value
    #screen.fill((0, 0, 0))
    screen.blit(background, (0,0))
    playerX += playerX_change
    # specifying the border
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # specifying the border for the enemy
    enemeyX += enemeyX_change
    if enemeyX <= 0:
        enemeyX_change = 3
        enemeyY += enemeyY_change
    elif enemeyX >= 736:
        enemeyX_change = -3
        enemeyY += enemeyY_change

    #Bullet movment
    if bullet_state is "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change

    print(playerX)
    player(playerX, playerY)
    enemey(enemeyX, enemeyY)
    pygame.display.update()