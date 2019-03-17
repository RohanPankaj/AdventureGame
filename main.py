import pygame

pygame.init()
screenWidth = 1000
screenLength = 1000
window = pygame.display.set_mode((screenLength, screenWidth))
pygame.display.set_caption("Adventure Game")

walk = [pygame.image.load("standing.PNG"),pygame.image.load("Walking1.PNG")]
background = pygame.image.load("background.PNG")
clock = pygame.time.Clock()
x = 50
y = 50
width = 40
height = 60
vel = 5

left = False
right = False
walk = False
walkCount = 0



run = True

def redrawGameWindow():
    global walkCount

    window.blit(background, (0,0))
    if walkCount + 1 > 27:
        walkCount = 0
    
    if walk:
        window.blit(walk[walkCount//2], (x, y))
        walkCount += 1
    '''else:
        window.blit(walk[walkCount], (x, y))
        walkCount += 1'''
    pygame.display.update()
while run:
    clock.tick(6)

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
    if controls[pygame.K_UP] and y > vel:
        y -= vel
        right = False
        left = False
    if controls[pygame.K_DOWN] and y < screenLength - height - vel:
        y += vel
        right = False
        LEft = False
    redrawGameWindow()
    
pygame.quit()
