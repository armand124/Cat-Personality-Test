from asyncio.proactor_events import constants
from stat import FILE_ATTRIBUTE_SPARSE_FILE
from tokenize import _all_string_prefixes
from typing import final
import pygame as picture
import sys
import random
import time as wait
from pygame_functions import *
from pygame import mixer
defaultWidth = 500
defaultHeight = 800
def GuiInit():
    picture.display.set_caption(os.path.join("assets","Cat Personality Test"))
    icon = picture.image.load(os.path.join("assets","icon.jpeg"))
    picture.display.set_icon(icon)
    picture.display.init()
GuiInit()

finalQuestions = []
merlin = 0
bingus = 0
floppa = 0
spoingus =0
finalChar = "none"
mixer.music.load(os.path.join("assets",'music.mp3'))
mixer.music.play()
screen = picture.display.set_mode((defaultWidth , defaultHeight))
last_update = picture.time.get_ticks()
#Gui basic initialization -> Going to update
questionsFloppa = ["You think you're better than everyone" , "You like showing off",
                   "You're usually the leader of the group" , "You'd throw a party right now"]
questionsBingus = ['You like to be in the center of attention' , "You're very sensitive to physical contact",
                    "You would do anything in your power to end the world","Everybody likes you"]
questionsSpoingus = ["You let people see your true emotions" , "People often call you cute and want to pet you",
                    "You cry very easily" , "You are dum dum"]
questionsMerlin = ["You feel the urge to fight someone daily" ,
                   "You don't like relationships" , "You don't care about apperance",
                   "You don't like being called cute"]

mainFont = os.path.join("assets",'orange juice 2.0.ttf')
#Needs to put this in class -> Font init
def makeQuestions():
    floppa1 = random.randint(0,3)
    floppa2 = random.randint(0,3)
    while floppa1==floppa2:
        floppa2= random.randint(0,3)
    global finalQuestions
    finalQuestions.append(questionsFloppa[floppa1])
    finalQuestions.append(questionsFloppa[floppa2])
    bingus1 = random.randint(0 , 3)
    bingus2 = random.randint(0  , 3)
    while bingus1==bingus2:
        bingus2=random.randint(0,3)
    finalQuestions.append(questionsBingus[bingus1])
    finalQuestions.append(questionsBingus[bingus2])
    spoingus1 = random.randint(0 , 3)
    spoingus2 = random.randint(0 , 3)
    while spoingus1==spoingus2:
        spoingus2 = random.randint(0 , 3)
    finalQuestions.append(questionsSpoingus[spoingus1])
    finalQuestions.append(questionsSpoingus[spoingus2])
    merlin1= random.randint(0 , 3)
    merlin2 = random.randint(0 , 3)
    while merlin1==merlin2:
        merlin2 = random.randint(0,3)
    finalQuestions.append(questionsMerlin[merlin1])
    finalQuestions.append(questionsMerlin[merlin2])
    random.shuffle(finalQuestions)
  
font = picture.font.Font(mainFont, 100)
font_for_second = picture.font.Font(mainFont , 70)
font_for_small = picture.font.Font(mainFont , 30)
first_welcome = font.render("Welcome!" , True , (255 , 255 , 255))
title = font_for_second.render("Cat Personality", True , (255 , 255 , 255))
startButton = picture.image.load(os.path.join("assets","startButton.png")).convert_alpha()
startYellow = picture.image.load(os.path.join("assets","startButtonYellow.png")).convert_alpha()
notPressSkip = picture.image.load(os.path.join("assets","notPressedSkip.png")).convert_alpha()
pressSkip = picture.image.load(os.path.join("assets","pressedSkip.png")).convert_alpha()
extSecond = font_for_second.render("Test", True , (255 , 255 , 255))
buttonPressed = picture.image.load(os.path.join("assets","buttonPressed.png")).convert_alpha()
buttonUnPressed = picture.image.load(os.path.join("assets","buttonUnpressed.png")).convert_alpha()
submitPressed = picture.image.load(os.path.join("assets","submitPressed.png")).convert_alpha()
submitUnPressed = picture.image.load(os.path.join("assets","submitUnPressed.png")).convert_alpha()
exitButtonNot = picture.image.load(os.path.join("assets","exitButton2.png")).convert_alpha()
exitButton = picture.image.load(os.path.join("assets","exitButton1.png")).convert_alpha()
congrats = font_for_second.render("Congratulations!" , True , (255 , 255 , 255))
bingusPng = picture.image.load(os.path.join("assets" , "bingusCat.png")).convert_alpha()
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
        goBackButton = Button(400 , 0 , notPressSkip)
        if goBackButton.buttonPressed():
            goBackButton =Button(400 , 0 , pressSkip)
        else:
            goBackButton = Button(400 , 0 , notPressSkip)
        goBackButton.showButton()
        questionsFont = picture.font.Font(mainFont , 55)
        if finalQuestions[case-3] == "You're very sensitive to physical contact":
            question1 = questionsFont.render("You're very sensitive", True , (255 , 255 , 255))
            question2 = questionsFont.render("to physical contact" , True , (255 , 255 ,255))
            screen.blit(question1 , (20 , 240))
            screen.blit(question2 , (30 , 285))
        if finalQuestions[case-3] == "You like to be in the center of attention":
            question1 = questionsFont.render("You like to be in the", True , (255 , 255 , 255))
            question2 = questionsFont.render("center of attention" , True , (255 , 255 ,255))
            screen.blit(question1 , (35 , 240))
            screen.blit(question2 , (33 , 285))
        if finalQuestions[case-3] == "You like showing off":
            question1= questionsFont.render("You like showing off", True , (255 , 255 , 255))
            screen.blit(question1 , (25 , 270))
        if finalQuestions[case-3] == "You would do anything in your power to end the world" :
           questionsFont = picture.font.Font(mainFont , 50)
           question1 = questionsFont.render("You would do anything", True , (255 , 255 , 255))
           question2 = questionsFont.render("in your power to destroy" , True , (255 , 255 ,255))
           question3 = questionsFont.render("the world" , True , (255 , 255 , 255))
           screen.blit(question1 , (18 , 240))
           screen.blit(question2 , (5 , 285)) 
           screen.blit(question3 , (145 , 330))
        if finalQuestions[case-3] == "You think you're better than everyone":
            aux = picture.font.Font(mainFont , 53)
            question1 = aux.render("You think you're better", True , (255 , 255 , 255))
            question2 = questionsFont.render("than everyone" , True , (255 , 255 ,255))
            screen.blit(question1 , (10 , 270))
            screen.blit(question2 , (90 , 315))
        if finalQuestions[case-3] == "You're usually the leader of the group":
            aux = picture.font.Font(mainFont , 55)
            question1 = aux.render("You're usually the", True , (255 , 255 , 255))
            question2 = questionsFont.render("leader of the group" , True , (255 , 255 ,255))
            screen.blit(question1 , (47 , 280))
            screen.blit(question2 , (28 , 325))  
        if finalQuestions[case-3] == "Everybody likes you":
            aux = picture.font.Font(mainFont , 55)
            question = questionsFont.render("Everybody likes you" , True , (255 , 255 ,255))
            screen.blit(question , (26 , 288))  
        if finalQuestions[case-3] == "You'd throw a party right now":
            aux = picture.font.Font(mainFont , 55)
            question = questionsFont.render("You'd throw a party" , True , (255 , 255 ,255))
            question1 = questionsFont.render("right now" , True , (255 , 255 ,255))
            screen.blit(question , (25 , 288))
            screen.blit(question1 , (142 , 333))
        if finalQuestions[case-3] == "You let people see your true emotions":
            aux = picture.font.Font(mainFont , 53)
            question1 = aux.render("You let people see your", True , (255 , 255 , 255))
            question2 = questionsFont.render("true emotions" , True , (255 , 255 ,255))
            screen.blit(question1 , (5 , 270))
            screen.blit(question2 , (90 , 315))
        if finalQuestions[case-3] == "People often call you cute and want to pet you" :
           questionsFont = picture.font.Font(mainFont , 50)
           question1 = questionsFont.render("People often call you", True , (255 , 255 , 255))
           question2 = questionsFont.render("cute and want to" , True , (255 , 255 ,255))
           question3 = questionsFont.render("pet you" , True , (255 , 255 , 255))
           screen.blit(question1 , (40 , 240))
           screen.blit(question2 , (72 , 285)) 
           screen.blit(question3 , (165 , 330))
        if finalQuestions[case-3] == "You cry very easily":
            question1= questionsFont.render("You cry very easily", True , (255 , 255 , 255))
            screen.blit(question1 , (43 , 285))
        if finalQuestions[case-3] == "You are dum dum":
            question1= questionsFont.render("You are dum dum", True , (255 , 255 , 255))
            screen.blit(question1 , (55 , 285))
        if finalQuestions[case-3] == "You feel the urge to fight someone daily":
            question1 = questionsFont.render("You feel the urge to", True , (255 , 255 , 255))
            question2 = questionsFont.render("fight someone daily" , True , (255 , 255 ,255))
            screen.blit(question1 , (30 , 260))
            screen.blit(question2 , (30 , 305))
        if finalQuestions[case-3] == "You don't like relationships":
            question1 = questionsFont.render("You don't like", True , (255 , 255 , 255))
            question2 = questionsFont.render("relationships" , True , (255 , 255 ,255))
            screen.blit(question1 , (95 , 260))
            screen.blit(question2 , (95 , 305))
        if finalQuestions[case-3] == "You don't care about apperance":
            aux = picture.font.Font(mainFont , 55)
            question1 = aux.render("You don't care about", True , (255 , 255 , 255))
            question2 = questionsFont.render("apperance" , True , (255 , 255 ,255))
            screen.blit(question1 , (18 , 270))
            screen.blit(question2 , (123 , 315))
        if finalQuestions[case-3] == "You don't like being called cute":
            question1 = questionsFont.render("You don't like being", True , (255 , 255 , 255))
            question2 = questionsFont.render("called cute" , True , (255 , 255 ,255))
            screen.blit(question1 , (28 , 260))
            screen.blit(question2 , (120 , 305))
        if submit.buttonPressed() and pressed:
            global floppa
            global bingus
            global merlin
            global spoingus
            if finalQuestions[case-3] == "You're very sensitive to physical contact":
                if h1_1:
                    floppa += 100
                if h1_2:
                    floppa += 60
                if h1_3:
                 
                    merlin+=40
                    floppa+=20
                if h1_4:
                
                    spoingus+=10
                    bingus +=50
                if h1_5:
                   
                    spoingus+=20
                    bingus+=100
            if finalQuestions[case-3] == "You like to be in the center of attention":
                if h1_1:
                  
                    spoingus+=50
                    merlin+=100
                if h1_2:
                    
                    spoingus+=30
                    merlin+=50
                if h1_3:
                  
                    spoingus+=10
                if h1_4:
                    
                    bingus+=30
                    floppa+=50
                if h1_5:
                    
                    bingus+=60
                    floppa+=100
            if finalQuestions[case-3] == "You like showing off":
                if h1_1:
                    spoingus+=100
                    merlin+=20
                if h1_2:
                   
                    spoingus+=50
                    merlin+=50
                if h1_3:
                    merlin+=70
                if h1_4:
                    
                    bingus+=30
                    floppa+=50
                if h1_5:
                  
                    bingus+=60
                    floppa+=100
            if finalQuestions[case-3] == "You would do anything in your power to end the world" :
                if h1_1:
                    spoingus+=100
                    floppa+=50
                if h1_2:
                    spoingus+=50
                    floppa+=25
                if h1_3:
                    merlin+=10
                    bingus+=10
                if h1_4:
                    bingus+=30
                    merlin+=50
                if h1_5:
                    bingus+=60
                    merlin+=100
            if finalQuestions[case-3] == "You think you're better than everyone":
                if h1_1:
                    spoingus+=100
                    bingus+=50
                if h1_2:
                    spoingus+=50
                    bingus+=25
                if h1_3:
                    merlin+=10
                    floppa+=10
                if h1_4:
                    merlin+=30
                    floppa+=50
                if h1_5:
                    merlin+=60
                    floppa+=100
            if finalQuestions[case-3] == "You're usually the leader of the group":
                if h1_1:
                    spoingus+=100
                    bingus+=50
                if h1_2:
                    spoingus+=50
                    bingus+=25
                if h1_3:
                    merlin+=10
                    floppa+=10
                if h1_4:
                    merlin+=30
                    floppa+=50
                if h1_5:
                    merlin+=60
                    floppa+=100
            if finalQuestions[case-3] == "Everybody likes you":
                if h1_1:
                    merlin+=100
                    floppa+=50
                if h1_2:
                    merlin+=50
                    floppa+=25
                if h1_3:
                    spoingus+=10
                    bingus+=10
                if h1_4:
                    bingus+=30
                    spoingus+=50
                if h1_5:
                    bingus+=60
                    spoingus+=100
            if finalQuestions[case-3] == "You'd throw a party right now":
                if h1_1:
                    merlin+=100
                    spoingus+=50
                if h1_2:
                    merlin+=50
                    spoingus+=25
                if h1_3:
                    floppa+=10
                    bingus+=10
                if h1_4:
                    bingus+=30
                    floppa+=50
                if h1_5:
                    bingus+=60
                    floppa+=100
            if finalQuestions[case-3] == "You let people see your true emotions":
                if h1_1:
                    merlin+=100
                    floppa+=50
                if h1_2:
                    merlin+=50
                    floppa+=25
                if h1_3:
                    spoingus+=10
                    bingus+=10
                if h1_4:
                    bingus+=30
                    spoingus+=50
                if h1_5:
                    bingus+=60
                    spoingus+=100
            if finalQuestions[case-3] == "People often call you cute and want to pet you" :
                if h1_1:
                    floppa+=100
                    merlin+=50
                if h1_2:
                    floppa+=50
                    merlin+=25
                if h1_3:
                    spoingus+=10
                    bingus+=10
                if h1_4:
                    bingus+=30
                    spoingus+=50
                if h1_5:
                    bingus+=60
                    spoingus+=100
            if finalQuestions[case-3] == "You cry very easily":
                if h1_1:
                    floppa+=100
                    merlin+=50
                if h1_2:
                    floppa+=50
                    merlin+=25
                if h1_3:
                    spoingus+=10
                    bingus+=10
                if h1_4:
                    bingus+=30
                    spoingus+=50
                if h1_5:
                    bingus+=60
                    spoingus+=100
            if finalQuestions[case-3] == "You are dum dum":
                if h1_1:
                    floppa+=100
                    bingus+=50
                if h1_2:
                    floppa+=50
                    bingus+=25
                if h1_3:
                    spoingus+=10
                    merlin+=10
                if h1_4:
                    spoingus+=50
                    merlin+=30
                if h1_5:
                    spoingus+=100
                    merlin+=60
            if finalQuestions[case-3] == "You feel the urge to fight someone daily":
                if h1_5:
                    merlin+=100
                    floppa+=50
                if h1_4:
                    merlin+=50
                    floppa+=25
                if h1_3:
                    spoingus+=10
                    bingus+=10
                if h1_2:
                    bingus+=30
                    spoingus+=50
                if h1_1:
                    bingus+=60
                    spoingus+=100
            if finalQuestions[case-3] == "You don't like relationships":
                if h1_1:
                    floppa+=100
                    spoingus+=50
                if h1_2:
                    floppa+=50
                    spoingus+=25
                if h1_3:
                    merlin+=10
                    bingus+=10
                if h1_4:
                    bingus+=30
                    merlin+=50
                if h1_5:
                    bingus+=60
                    merlin+=100
            if finalQuestions[case-3] == "You don't care about apperance":
                if h1_1:
                    floppa+=100
                    spoingus+=50
                if h1_2:
                    floppa+=50
                    spoingus+=25
                if h1_3:
                    merlin+=10
                    bingus+=10
                if h1_4:
                    bingus+=30
                    merlin+=50
                if h1_5:
                    bingus+=60
                    merlin+=100
            if finalQuestions[case-3] == "You don't like being called cute":
                if h1_1:
                    floppa+=100
                    spoingus+=50
                if h1_2:
                    floppa+=50
                    spoingus+=25
                if h1_3:
                    merlin+=10
                    bingus+=10
                if h1_4:
                    bingus+=30
                    merlin+=50
                if h1_5:
                    bingus+=60
                    merlin+=100
            submit = Button(70 , 550 , submitPressed)
        else:
            submit = Button(70 , 550 , submitUnPressed)
        screen.blit(mes0,(37 ,483))
        screen.blit(mes5 , (439 , 483))
        submit.showButton()
        bt1.showButton()
        bt2.showButton()
        bt3.showButton()
        bt4.showButton()
        bt5.showButton()
    picture.display.update()
def endingScreenMerlin():
    screen.fill((0 , 141 , 131))
    you_are = font_for_second.render("You are Merlin", True , (255 , 255 ,255))
    merlinPng = picture.image.load(os.path.join("assets","merlinCat.png")).convert_alpha()
    bing = Button(126 , 300 , merlinPng)
    bye = Button(210 , 600 , notPressSkip)
    if bye.buttonPressed():
        bye =Button(210 , 600 , exitButton)
    else:
        bye = Button(210 , 600 , exitButtonNot)
    bye.showButton()
    bing.showButton()
    screen.blit(congrats,(7 , 100))
    screen.blit(you_are,(50 , 200))
    picture.display.update()
def endingScreenFloppa():
    screen.fill((0 , 141 , 131))
    you_are = font_for_second.render("You are Floppa", True , (255 , 255 ,255))
    floppaPng = picture.image.load(os.path.join("assets","floppaCat.png")).convert_alpha()
    bing = Button(126 , 300 , floppaPng)
    bye = Button(210 , 600 , notPressSkip)
    if bye.buttonPressed():
        bye =Button(210 , 600 , exitButton)
    else:
        bye = Button(210 , 600 , exitButtonNot)
    bye.showButton()
    bing.showButton()
    screen.blit(congrats,(7 , 100))
    screen.blit(you_are,(38 , 200))
    picture.display.update()
def endingScreenBingus():
    screen.fill((0 , 141 , 131))
    you_are = font_for_second.render("You are Bingus", True , (255 , 255 ,255))
    bing = Button(126 , 300 , bingusPng)
    bye = Button(210 , 600 , notPressSkip)
    if bye.buttonPressed():
        bye =Button(210 , 600 , exitButton)
    else:
        bye = Button(210 , 600 , exitButtonNot)
    bye.showButton()
    bing.showButton()
    screen.blit(congrats,(7 , 100))
    screen.blit(you_are,(45 , 200))
    picture.display.update()
def endingScreenSpoingus():
    screen.fill((0 , 141 , 131))
    you_are = font_for_second.render("You are Spoingus", True , (255 , 255 ,255))
    spoingusPng = picture.image.load(os.path.join("assets","spoingusCat.png")).convert_alpha()
    bing = Button(126 , 300 , spoingusPng)
    bye = Button(210 , 600 , notPressSkip)
    if bye.buttonPressed():
        bye =Button(210 , 600 , exitButton)
    else:
        bye = Button(210 , 600 , exitButtonNot)
    bye.showButton()
    bing.showButton()
    screen.blit(congrats,(7 , 100))
    screen.blit(you_are,(8 , 200))
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
bye = Button(210 , 600 , exitButtonNot)
answearButton1 = Button(30 , 450 , buttonUnPressed)
       
start_button = Button(80 , 320 , startButton)
second_start_button = Button(80,320 , startYellow)
goBackButton = Button(400 , 0 , notPressSkip)
submit = Button (70 , 550 , submitUnPressed)
bt1 = Button(30 , 450 , buttonPressed)
bt2 = Button(130 , 450 , buttonUnPressed)
bt3 = Button(230 , 450 , buttonUnPressed)
bt4 = Button(330 , 450 , buttonUnPressed)
bt5 = Button(430 , 450 , buttonUnPressed)
def click():
    clickSound = mixer.Sound(os.path.join("assets","effect.mp3"))
    clickSound.play()
case = 1
running = True
while case<11:
  if case == 10:
      maximum = []
      maximum.append(merlin)
      maximum.append(floppa)
      maximum.append(spoingus)
      maximum.append(bingus)
      maximum.sort()
      if merlin==floppa or floppa==bingus:
          floppa = -1
      if merlin==spoingus or spoingus==floppa or spoingus==bingus:
          spoingus= -2
      if bingus==merlin:
          merlin = -3
      if maximum[3] == merlin:
          endingScreenMerlin()
      if maximum[3] == floppa:
          endingScreenFloppa()
      if maximum[3] == bingus:
          endingScreenBingus()
      if maximum[3] == spoingus:
          endingScreenSpoingus()
      picture.time.wait(100)
      if bye.buttonPressed():
          click()
          picture.time.wait(200)
          case = 404     
  elif case<11:      
    ScreenUpdate(case)
    if submit.buttonPressed() and pressed:      
        case = case + 1
        click()
        picture.time.wait(200)
        pressed = False
        h1 = False
        h2 = False
        h3 = False
        h4 = False
        h5 = False
        if goBackButton.buttonPressed():
          click()
          picture.time.wait(200)
          case = 1 
    if case==1 and second_start_button.buttonPressed() :
        click()
        finalQuestions = []
        merlin = 0
        floppa = 0
        bingus =0
        spoingus =0
        makeQuestions()
        picture.time.wait(200)
        case = 2
    if goBackButton.buttonPressed() and case>=2:
        click()
        picture.time.wait(200)
        h1 = False
        h2 = False
        h3 = False
        h4 = False
        h5 = False
        pressed = False
        case = 1    
  for event in picture.event.get():
    if event.type == picture.QUIT:
        sys.exit()


