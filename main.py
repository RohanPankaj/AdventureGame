import pygame

pygame.init()
screenWidth = 1000
screenLength = 1000
window = pygame.display.set_mode((screenLength, screenWidth))
pygame.display.set_caption("Adventure Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

standing = pygame.image.load('standing.png')

background = [pygame.image.load("rightRoom.PNG"), pygame.image.load("normalRoom.PNG"),pygame.image.load("leftRoom.PNG")]

clock = pygame.time.Clock()
x = 50
y = 50
width = 40
height = 60
vel = 5

left = False
right = False

walkCount = 0



run = True

def redrawGameWindow():
    global walkCount

    window.blit(background[1], (0,0))
   
    if walkCount + 1 >= 27:
        walkCount = 0
    
    if right:
        window.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    
    elif left:
        window.blit(walkLeft[walkCount//3], (x,y))
        walkCount +=1
    else:
        window.blit(standing,(x,y))
    '''else:
        window.blit(walk[walkCount], (x, y))
        walkCount += 1'''
    pygame.display.update()
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    controls = pygame.key.get_pressed()
    
    if controls[pygame.K_RIGHT] and x < screenWidth - width - vel:
        x += vel
        right = True
        left = False
    elif controls[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    else:
        right = False
        left = False
        walkCount = 0
    '''if controls[pygame.K_UP] and y > vel:
        y -= vel
        right = False
        left = False
    if controls[pygame.K_DOWN] and y < screenLength - height - vel:
        y += vel
        right = False
        LEft = False'''
    redrawGameWindow()
    
pygame.quit()