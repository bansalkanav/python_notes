import time

import pygame

# initiating pygame
pygame.init()

display_width = 800
display_height = 500

# Picking the resolution of our display
surface = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Helicopter')

black = (0, 0, 0)  # RGB
white = (255, 255, 255)

helicopter = pygame.image.load('Helicopter.png')
x = 150
y = 200

y_move = 0

####################################


def Helicopter(x, y):
    surface.blit(helicopter, (x, y))


# def msgSurface(text):
#     smallText = pygame.font.Font('freesansbold.ttf', 20)
#     largeText = pygame.font.Font('freesansbold.ttf', 150)
#
#     titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
#     titleTextRect.center = display_width/2, display_height/2
#     surface.blit(titleTextSurf, titleTextRect)
#
#     typTextSurf, typTextRect = makeTextObjs('Press any key to continue', smallText)
#     titleTextRect.center = display_width/2, ((display_height/2)+100)
#     surface.blit(typTextSurf, typTextRect)
#
#     pygame.display.update()
#     time.sleep(1)
#


def gameOver():
    # msgSurface('Kaboom!')
    quit()


####################################

# Measuring FPS-Frame per seconds
clock = pygame.time.Clock()

# Creating a game loop which will run many times a second
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        ###################################
        if event.type == pygame.KEYDOWN:  # if a key is pressed
            if event.key == pygame.K_UP:  # if that key is UP arrow key
                y_move = -5
        if event.type == pygame.KEYUP:  # if we released a key
            if event.key == pygame.K_UP:
                y_move = 5
        ###################################

    y += y_move  # y = y + y_move

    surface.fill(black)
    Helicopter(x, y)

    if y > display_height-43 or y < 0:
        gameOver()

    pygame.display.update()  # update the display
    clock.tick(60)  # run the above code 60 times per second

pygame.quit()

quit()
