from asyncio.proactor_events import constants
import pygame as picture
import sys
defaultWidth = 500
defaultHeight = 800
picture.init()
screen = picture.display.set_mode((defaultWidth , defaultHeight))

#Gui basic initialization -> Going to update
def GuiInit():
    picture.display.set_caption("Cat Personality Test")
    icon = picture.image.load('icon.jpeg')
    picture.display.set_icon(icon)
    picture.display.init()

#Needs to put this in class -> Font init
font = picture.font.Font('freesansbold.ttf', 65)
font_for_second = picture.font.Font('freesansbold.ttf' , 40)
first_welcome = font.render("Welcome!" , True , (255 , 255 , 255))
title = font_for_second.render("Cat Personality Test", True , (255 , 255 , 255))
startButton = picture.image.load("startButton.png").convert_alpha() #-> Need to change photo
#Function to update the screen with all it's assets
def screenUpdate():
    screen.fill((0 , 141 , 131))
    screen.blit(first_welcome,(90,100))
    screen.blit(title,(47,250))
    start_button.showButton()
    picture.display.update()
    
GuiInit()

class Button():
    def __init__(self , x , y , image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    
    def showButton(self):
        screen.blit(self.image , (self.rect.x , self.rect.y))

start_button = Button(80 , 320 , startButton)
running = True
while running:
    screenUpdate()
    for event in picture.event.get():
        if event.type == picture.QUIT:
            sys.exit()



