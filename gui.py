from asyncio.proactor_events import constants
from stat import FILE_ATTRIBUTE_SPARSE_FILE
from tokenize import _all_string_prefixes
import pygame as picture
import sys
import time as wait
from pygame_functions import *
from playsound import playsound
from pygame import mixer
defaultWidth = 500
defaultHeight = 800
def GuiInit():
    picture.display.set_caption("Cat Personality Test")
    icon = picture.image.load('icon.jpeg')
    picture.display.set_icon(icon)
    picture.display.init()
GuiInit()
mixer.music.load('music.mp3')
mixer.music.play()
screen = picture.display.set_mode((defaultWidth , defaultHeight))
last_update = picture.time.get_ticks()
#Gui basic initialization -> Going to update

mainFont = 'orange juice 2.0.ttf'
#Needs to put this in class -> Font init
font = picture.font.Font(mainFont, 100)
font_for_second = picture.font.Font(mainFont , 70)
font_for_small = picture.font.Font(mainFont , 30)
first_welcome = font.render("Welcome!" , True , (255 , 255 , 255))
title = font_for_second.render("Cat Personality", True , (255 , 255 , 255))
startButton = picture.image.load("startButton.png").convert_alpha()
startYellow = picture.image.load("startButtonYellow.png").convert_alpha()
notPressSkip = picture.image.load("notPressedSkip.png").convert_alpha()
pressSkip = picture.image.load("pressedSkip.png").convert_alpha()
extSecond = font_for_second.render("Test", True , (255 , 255 , 255))
buttonPressed = picture.image.load("buttonPressed.png").convert_alpha()
buttonUnPressed = picture.image.load("buttonUnpressed.png").convert_alpha()
submitPressed = picture.image.load("submitPressed.png").convert_alpha()
submitUnPressed = picture.image.load("submitUnPressed.png").convert_alpha()
mes0 =font_for_small.render("0" , True , (255 , 255 , 255))
mes5 =font_for_small.render("5" , True , (255 , 255 , 255))
#Function to update the screen with all it's assets
h1 = False
h2 = False
h3 = False
h4 = False
h5 = False
pressed = False
def ScreenUpdate(case):
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
            submit = False
            second_start_button.showButton()
        else:
            second_start_button = Button(80 , 320 , startButton)
            second_start_button.showButton()
    if case>=2:
        screen.fill((0 , 141 , 131))
        submit = Button(70 , 550 , submitUnPressed)
        global h1
        global h2
        global h3
        global h4
        global h5
        global pressed
        h1_1 = h1
        h1_2 = h2
        h1_3 = h3
        h1_4 = h4
        h1_5 = h5
        if h1_1:
            bt1 = Button(30 , 450 , buttonPressed)
            bt2 = Button(130 , 450 , buttonUnPressed)
            bt3 = Button(230 , 450 , buttonUnPressed)
            bt4 = Button(330 , 450 , buttonUnPressed)
            bt5 = Button(430 , 450 , buttonUnPressed)
        if h1_2:
            bt1 = Button(30 , 450 , buttonUnPressed)
            bt2 = Button(130 , 450 , buttonPressed)
            bt3 = Button(230 , 450 , buttonUnPressed)
            bt4 = Button(330 , 450 , buttonUnPressed)
            bt5 = Button(430 , 450 , buttonUnPressed)
        if h1_3:
            bt1 = Button(30 , 450 , buttonUnPressed)
            bt2 = Button(130 , 450 , buttonUnPressed)
            bt3 = Button(230 , 450 , buttonPressed)
            bt4 = Button(330 , 450 , buttonUnPressed)
            bt5 = Button(430 , 450 , buttonUnPressed)
        if h1_4:
            bt1 = Button(30 , 450 , buttonUnPressed)
            bt2 = Button(130 , 450 , buttonUnPressed)
            bt3 = Button(230 , 450 , buttonUnPressed)
            bt4 = Button(330 , 450 , buttonPressed)
            bt5 = Button(430 , 450 , buttonUnPressed)
        if h1_5:
            bt1 = Button(30 , 450 , buttonUnPressed)
            bt2 = Button(130 , 450 , buttonUnPressed)
            bt3 = Button(230 , 450 , buttonUnPressed)
            bt4 = Button(330 , 450 , buttonUnPressed)
            bt5 = Button(430 , 450 , buttonPressed)
        if h1_1 == False and h1_2 == False and h1_3 == False and h1_4 == False and h1_5 == False:
            bt1 = Button(30 , 450 , buttonUnPressed)
            bt2 = Button(130 , 450 , buttonUnPressed)
            bt3 = Button(230 , 450 , buttonUnPressed)
            bt4 = Button(330 , 450 , buttonUnPressed)
            bt5 = Button(430 , 450 , buttonUnPressed)
        if bt1.buttonPressed():
            pressed = True
            h1_1 = True
            h1_2 = False
            h1_3 = False
            h1_4 = False
            h1_5 = False
        if bt2.buttonPressed():
            pressed = True
            h1_1 = False
            h1_2 = True
            h1_3 = False
            h1_4 = False
            h1_5 = False
        if bt3.buttonPressed():
            pressed = True
            h1_1 = False
            h1_2 = False
            h1_3 = True
            h1_4 = False
            h1_5 = False
        if bt4.buttonPressed():
            pressed = True
            h1_1 = False
            h1_2 = False
            h1_3 = False
            h1_4 = True
            h1_5 = False
        if bt5.buttonPressed():
            pressed = True
            h1_1 = False
            h1_2 = False
            h1_3 = False
            h1_4 = False
            h1_5 = True
        h1 = h1_1
        h2 = h1_2
        h3 = h1_3
        h4 = h1_4
        h5 = h1_5
        if submit.buttonPressed() and pressed:
            submit = Button(70 , 550 , submitPressed)
        else:
            submit = Button(70 , 550 , submitUnPressed)
        goBackButton = Button(400 , 0 , notPressSkip)
        if goBackButton.buttonPressed():
            goBackButton =Button(400 , 0 , pressSkip)
        else:
            goBackButton = Button(400 , 0 , notPressSkip)
        goBackButton.showButton()
        screen.blit(mes0,(37 ,483))
        screen.blit(mes5 , (439 , 483))
        submit.showButton()
        bt1.showButton()
        bt2.showButton()
        bt3.showButton()
        bt4.showButton()
        bt5.showButton()
    picture.display.update()

                  
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

answearButton1 = Button(30 , 450 , buttonUnPressed)
       
#Coding questions
def writeInFile(name , score):
    with open ("session.txt" , 'w') as file:
        file.write(name)
        file.write(' ')
        file.write(score)
another = False

start_button = Button(80 , 320 , startButton)
second_start_button = Button(80,320 , startYellow)
goBackButton = Button(400 , 0 , notPressSkip)
submit = Button (70 , 550 , submitUnPressed)
bt1 = Button(30 , 450 , buttonPressed)
bt2 = Button(130 , 450 , buttonUnPressed)
bt3 = Button(230 , 450 , buttonUnPressed)
bt4 = Button(330 , 450 , buttonUnPressed)
bt5 = Button(430 , 450 , buttonUnPressed)

case = 1
running = True
while running:
    ScreenUpdate(case)
    if submit.buttonPressed():
        picture.time.wait(200)
        pressed = False
        h1 = False
        h2 = False
        h3 = False
        h4 = False
        h5 = False
        if goBackButton.buttonPressed():
         picture.time.wait(200)
         case = 1 
    if second_start_button.buttonPressed() :
        picture.time.wait(200)
        case = 2
    if goBackButton.buttonPressed():
        picture.time.wait(200)
        case = 1    
    for event in picture.event.get():
        if event.type == picture.QUIT:
            sys.exit()



