from asyncio.proactor_events import constants
from tokenize import _all_string_prefixes
import pygame as picture
import sys
import time as wait
from pygame_functions import *
from playsound import playsound
from pygame import mixer
defaultWidth = 500
defaultHeight = 800
picture.init()
mixer.music.load('music.mp3')
mixer.music.play()
screen = picture.display.set_mode((defaultWidth , defaultHeight))
last_update = picture.time.get_ticks()
#Gui basic initialization -> Going to update
def GuiInit():
    picture.display.set_caption("Cat Personality Test")
    icon = picture.image.load('icon.jpeg')
    picture.display.set_icon(icon)
    picture.display.init()

mainFont = 'orange juice 2.0.ttf'
#Needs to put this in class -> Font init
font = picture.font.Font(mainFont, 100)
font_for_second = picture.font.Font(mainFont , 70)
first_welcome = font.render("Welcome!" , True , (255 , 255 , 255))
title = font_for_second.render("Cat Personality", True , (255 , 255 , 255))
startButton = picture.image.load("startButton.png").convert_alpha()
startYellow = picture.image.load("startButtonYellow.png").convert_alpha()
notPressSkip = picture.image.load("notPressedSkip.png").convert_alpha()
pressSkip = picture.image.load("pressedSkip.png").convert_alpha()
extSecond = font_for_second.render("Test", True , (255 , 255 , 255))
#Function to update the screen with all it's assets
def screenUpdate(case):
    if case == 1:
        screen.fill((0 , 141 , 131))
        screen.blit(first_welcome,(45,100))
        screen.blit(title,(30,250))
        screen.blit(extSecond , (180 , 350))
        goBackButton = Button(400 , 0 , notPressSkip)
        if goBackButton.buttonPressed():
            goBackButton =Button(400 , 0 , pressSkip)
        else:
            goBackButton = Button(400 , 0 , notPressSkip)
        goBackButton.showButton()
        second_start_button = Button(80 , 320 , startYellow)
        if second_start_button.buttonPressed() :
            second_start_button = Button(80,320 , startYellow)
            second_start_button.showButton()
        else:
            second_start_button = Button(80 , 320 , startButton)
            second_start_button.showButton()
    if case == 2:
        screen.fill((0 , 141 , 131))
        goBackButton = Button(400 , 0 , notPressSkip)
        if goBackButton.buttonPressed():
            goBackButton =Button(400 , 0 , pressSkip)
        else:
            goBackButton = Button(400 , 0 , notPressSkip)
        goBackButton.showButton()

    picture.display.update()
    
GuiInit()

class Button():
    def __init__(self , x , y , image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    
    def showButton(self):
        screen.blit(self.image , (self.rect.x , self.rect.y))

    def buttonPressed(self):
        if self.rect.collidepoint(picture.mouse.get_pos()):
            if picture.mouse.get_pressed()[0]==1:
                return True
               
#Coding questions

start_button = Button(80 , 320 , startButton)
second_start_button = Button(80,320 , startYellow)
goBackButton = Button(400 , 0 , notPressSkip)
case = 1
running = True
while running:
    screenUpdate(case)
    if second_start_button.buttonPressed() :
        picture.time.wait(500)
        case = 2
    if goBackButton.buttonPressed():
        picture.time.wait(500)
        case = 1
    for event in picture.event.get():
        if event.type == picture.QUIT:
            sys.exit()



