#!/usr/bin/env python

"""
Hi everyone 
This is a simple car game developed using pygame witn python 3

"""
__author__  = "Mohamed Hamidat, C# and python Developer, hamidatmohamed@yahoo.fr"

import pygame
import time
import random 



#display dimension
display_width = 800
display_height = 600

#car dimension
car_width = 70
car_height = 140

#colors 
black = (0,0,0)
white = (255,255,255)
blue =(53, 115, 255)
red = (200,0,0)
green = (0, 200, 0)
bright_red = (255,0,0)
bright_green = (0,255,0)
pause = False
score_game = 0

game_display = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
#game setup 
def game_init():
    pygame.init()
    pygame.display.set_caption('Fast_and_Curious/Mohamed')
    
    #game_icon = pygame.image.load('carIcon.png')
    #pygame.display.set_icon(game_icon)

#backgroundImg = pygame.image.load ('way.png')

##############---------FONCTIONS--------------##################

def display(count, x, y, message_format = 'Dodged: %d'):
    """display the score"""
   # max_dodged = 10 
    font = pygame.font.SysFont("comicsansms", 20)
    text = font.render(message_format%count, True, black)
    game_display.blit(text, (x, y))

def things(thingX, thingY, thingW, thingH, color):
    """draw random things (car or anything)""" 
    pygame.draw.rect(game_display, color, [thingX, thingY, thingW, thingH])


def line(lineX, lineY, lineW, lineH, color):
    """draw way lines """ 
    pygame.draw.rect(game_display, color, [lineX, lineY, lineW, lineH])


def load_image(x , y, image_name):
    img = pygame.image.load(image_name)
    game_display.blit(img, (x, y))

def text_object(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    """display message after crash"""
    largeText = pygame.font.SysFont("comicsansms",115)
    textSurf, textRect = text_object(text, largeText)
    textRect.center = ((display_width/2) , (display_height/2))
    game_display.blit(textSurf, textRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash(x, y):
    car_crash = pygame.image.load('images/carcrash.png')
    game_display.blit(car_crash, ((x - 45), (y - 30)))
    crash_sound = pygame.mixer.Sound("music/crash.wav")
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    largeText = pygame.font.SysFont("comicsansms",90)
    textSurf, textRect = text_object("You Crashed!", largeText)
    textRect.center = ((display_width/2) , (display_height/4))
    game_display.blit(textSurf, textRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        

        button("Play Again", 150,250,100,50, green, bright_green, game_loop)
        button("Quit", 550,250,100,50, red, bright_red, quitgame)


        pygame.display.update()
        clock.tick(15)


def button(msg, x, y, w, h, ic, ac, action=None): 
    """message, dimension, active/inactive color"""

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(mouse)

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(game_display, ac,(x, y,w,h))
        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(game_display, ic,(x, y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_object(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    game_display.blit(textSurf, textRect)


def quitgame():
    pygame.quit()
    quit()

def game_unpause():
    global pause
    pause = False

def game_pause():
    ############
    pygame.mixer.music.pause()
    #############
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",90)
        textSurf, textRect = text_object("Pause!", largeText)
        textRect.center = ((display_width/2) , (display_height/4))
        game_display.blit(textSurf, textRect)

        button("Continue !", 150,250,100,50, green, bright_green, game_unpause)
        button("Quit", 550,250,100,50, red, bright_red, quitgame)


        pygame.display.update()
        clock.tick(15)


def game_intro():

    pygame.mixer.music.load("music/atlanta.wav")
    pygame.mixer.music.play(-1)

    intro = True 

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        game_display.fill(white)         
    
        largeText = pygame.font.SysFont("comicsansms",80)
        textSurf, textRect = text_object("Let's Ride !", largeText)
        textRect.center = ((display_width/2) , (display_height/2))
        game_display.blit(textSurf, textRect)

        button("GO !", 150,450,100,50, green, bright_green, game_loop)
        button("Quit", 550,450,100,50, red, bright_red, quitgame)


        pygame.display.update()
        clock.tick(15)

def game_loop():
    global pause
    global score_game

    pygame.mixer.music.load('music/coffee_stains.wav')
    pygame.mixer.music.play(-1)

    x = (display_width * 0.45)
    y = (display_height * 0.75)

    x_change = 0
    y_change = 0
    speed_change = 0

    thing_width = 70
    thing_height = 140

    thing_startx = random.randrange(100, display_width - 200)
    thing_starty = -600
    thing_speed = 4 

    lineX = 400
    lineY = 0
    lineW = 20 
    lineH = 450
    line_speed = 10

    tree_y_right = 600
    tree_y_left = 300
    tree_h = 600 
    tree_speed = 10

    dodged = 0 

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type== pygame.KEYDOWN:

                if event.key==pygame.K_LEFT:
                    x_change=-5
                if event.key == pygame.K_RIGHT:
                    x_change=5

                if event.key == pygame.K_p:
                    pause = True
                    game_pause()
                    
            if event.type == pygame.KEYUP:
                x_change= 0
        x += x_change

        game_display.fill(white)         
        
        line(150, 0, 20, display_height, blue)
        line(display_width-150, 0, 20, display_height, blue)

        load_image(thing_startx, thing_starty, 'images/car.png')
        load_image(80, tree_y_left, 'images/trees.jpg')
        load_image(700, tree_y_right, 'images/trees.jpg')
        load_image(x,y, 'images/car1.png')

        thing_starty += thing_speed
        lineY += line_speed
        tree_y_left += tree_speed
        tree_y_right += tree_speed

        display(dodged, 5, 25)
        display(thing_speed*60 , 5, 50, "Spd: %d px/s")    
        display(score_game, 5, 5, "Final Score: %d")

        if x > display_width - car_width - 150 or x < 150 :
            # 100 way background image
            crash(x,y)
        
        if thing_starty > display_height :
            thing_starty = 0 - thing_height # reset y 
            thing_startx = random.randrange(170, display_width-thing_width-150)
            dodged += 1 
            score_game += 1
            thing_speed += 1/20 # accelarate       

        if lineY > display_height  :
            lineY = 0 - lineH # reset y 
            thing_speed += 1/15

        if tree_y_left > display_height  :
            tree_y_left = 0 - tree_h # reset y 
            thing_speed += 1/15

        if tree_y_right > display_height  :
            tree_y_right = 0 - tree_h # reset y 
            thing_speed += 1/15

        ### check crash  
        if y < (thing_starty + thing_height) and y+ car_height >= thing_starty + thing_height:
            if x > thing_startx and x < (thing_startx + thing_width) or x + car_width > thing_startx \
            and x + car_width < thing_startx + thing_width :
                crash(x, y)

        pygame.display.update()
        clock.tick(60)

def main():
    game_init()
    game_intro()
    game_loop()
    pygame.quit()
    quit() 

if __name__ == '__main__':
    main()


