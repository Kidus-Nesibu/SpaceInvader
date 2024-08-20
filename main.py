import pygame
import random
import math

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
enemeyimg =[]
enemeyX = []
enemeyY = []
enemeyX_change = []
enemeyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemeyimg.append(pygame.image.load('enemy.png'))
    enemeyX.append(random.randint(0, 735))
    enemeyY.append(random.randint(50, 150))
    enemeyX_change.append(3)
    enemeyY_change.append(40)

#Bullet
bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

#Score
Score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32, )
textX = 10
textY = 10

def show_score(x, y):
    score = font.render("Score:"+ str(Score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def player(x, y):
    # blit means draw
    screen.blit(playerimg,(x, y))
def enemey(x, y, i):
    screen.blit(enemeyimg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))

def isCollision(enemeyX, enemeyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemeyX - bulletX, 2)) + (math.pow(enemeyY - bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

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
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

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
    for i in range(num_of_enemies):
        enemeyX[i] += enemeyX_change[i]
        if enemeyX[i] <= 0:
            enemeyX_change[i] = 3
            enemeyY[i] += enemeyY_change[i]
        elif enemeyX[i] >= 736:
            enemeyX_change[i] = -3
            enemeyY[i] += enemeyY_change[i]

    #Collision
        Collision = isCollision(enemeyX[i], enemeyY[i], bulletX, bulletY)
        if Collision:
            bulletY = 480
            bullet_state = "ready"
            Score_value += 1
            enemeyX[i] = random.randint(0, 735)
            enemeyY[i]= random.randint(50, 150)

        enemey(enemeyX[i], enemeyY[i], i)
    #Bullet movment
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change



    print(playerX)
    player(playerX, playerY)
    show_score(textX, textY )
    pygame.display.update()