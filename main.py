import pygame

pygame.init()
screenWidth = 1000
screenLength = 1000
window = pygame.display.set_mode((screenLength, screenWidth))
pygame.display.set_caption("Adventure Game")

#declare sprites
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
standing = pygame.image.load('standing.png')
background = [pygame.image.load("rightRoom.PNG"), pygame.image.load("normalRoom.PNG"),pygame.image.load("leftRoom.PNG")]


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

#initialize variables
clock = pygame.time.Clock()


run = True
user = player(300, 410, 64, 64)  
def redrawGameWindow():
    window.blit(background[0], (0,0))
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
    
    redrawGameWindow()
    
pygame.quit()
