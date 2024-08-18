import pygame
from pygame import KEYDOWN, K_LEFT, K_RIGHT, KEYUP

#initialize the pygame
pygame.init()
# creates the screen
screen = pygame.display.set_mode((800,600))
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

def player(x, y):
    # blit means draw
    screen.blit(playerimg,(x, y))

#Game loop
running = True
while running:
    for event in pygame.event.get(): # this method gives me the event that are happening in the pygame window
        if event.type == pygame.QUIT:
            running = False
    # if keystroke is pressed checks whether its right or left
        if event.type == pygame.KEYDOWN:
            print("A keystroke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_change -= 3
            elif event.key == pygame.K_RIGHT:
                playerX_change += 3

        if event.type == KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                print("key stroke is released")

            #this function accepts rgb value
        screen.fill((0, 0, 0))
        playerX += playerX_change
        print(playerX)
        player(playerX, playerY)
        pygame.display.update()

