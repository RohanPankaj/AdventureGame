import pygame
import random

pygame.init()
screenWidth = 600
screenLength = 600
window = pygame.display.set_mode((screenLength, screenWidth))
pygame.display.set_caption("Adventure Game")

#declare sprites
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
standing = pygame.image.load('standing.png')
background = [pygame.image.load("leftRoom.PNG"), pygame.image.load("normalRoom.PNG"),pygame.image.load("rightRoom.PNG")]
boss = [pygame.image.load("L1E.png")]
rooms = [0, 1, 2, 3, 4]

def ShowBoss(bossRoom):
    global backgroundNumber
    if backgroundNumber == bossRoom:
        window.blit(boss[0], (300,500))
    #else:
        
backpack = []
objects = ["sword", "magic beans"]
class player(object):
    def __init__ (self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.walkCount = 0
        self.right = False
        self.left = False
        self.backgroundNumber = 0

    def draw(self, window):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.right:
            window.blit(walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif self.left:
            window.blit(walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount +=1
        else:
            window.blit(standing,(self.x, self.y))
'''class stage(object):
    
    def __init__(self, x, roomNumber, backgroundNumber):
        self.x = x
        self.roomnumber = 1
        self.backgroundNumber = 1
    
    
    def changeBackground(self, x, roomNumebr, backgroundNumber):
        if self.x >= 500:
            self.roomNumber += 1
        elif self.x <= 100:
            self.roomNumber -+ 1
        if self.roomNumber == 4:
            self.backgroundNumber = 2
        elif self.roomNumber ==2:
            self.backgroundNumber = 0'''
#initialize variables
clock = pygame.time.Clock()
gameReset = True
roomNumber = 1
backgroundNumber = 0
run = True
user = player(250, 530, 64, 64)  
bossRoom = random.choice(rooms)
#stage = stage(user.x, 1, 1)
def redrawGameWindow():
    global gameReset
    global backgroundNumber
    if gameReset:
        window.blit(background[0], (0,0))
        user.draw(window)
        pygame.display.update()
        gameReset = False
    elif gameReset == False:
        if roomNumber == 6:
            backgroundNumber = 2
        elif roomNumber == 1:
            backgroundNumber = 0
        else:
            backgroundNumber = 1
        window.blit(background[backgroundNumber], (0,0))
        user.draw(window)
        pygame.display.update()

    window.blit(background[backgroundNumber], (0,0))
    user.draw(window)
    pygame.display.update()        

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    controls = pygame.key.get_pressed()
    
    if controls[pygame.K_RIGHT] and user.x < screenWidth - user.width - user.vel:
        user.x += user.vel
        user.right = True
        user.left = False
    elif controls[pygame.K_LEFT] and user.x > user.vel:
        user.x -= user.vel
        user.left = True
        user.right = False
    else:
        user.right = False
        user.left = False
        user.walkCount = 0
    if user.x >= 500 and backgroundNumber != 2:
            roomNumber += 1
            user.x = 100
    elif user.x <= 100  and backgroundNumber != 0:
            roomNumber -= 1
            user.x = 500
   
    redrawGameWindow()
    ShowBoss(bossRoom)
   
pygame.quit()



#Copyright © Rohan Pankaj Adapted form Tech with Ted Tutorial