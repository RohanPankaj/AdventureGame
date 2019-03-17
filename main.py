import pygame

pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Adventure Game")

#Sprtie Height and velocity
x = 50
y = 50
width = 40
height = 60
vel = 5

run = True

#Getting what keyboard keys are being pressed
controls = pygame.key.get_pressed()

#Main Loop
while run:
    pygame.time.delay(100)
    #Close program when x clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False\
    #Movement Controls            
    if controls[pygame.K_RIGHT]:
        x += vel
    if controls[pygame.K_LEFT]:
        x -= vel
    if controls[pygame.K_UP]:
        y -= vel
    if controls[pygame.K_DOWN]:
        y += vel
    #reset window so sprtie looks like it is moving
    window.fill((0, 0, 0))
    #Set siprite color and size
    pygame.draw.rect(window, (255, 255, 255), (x, y, width, height))
    #Update screen
    pygame.display.update()
pygame.quit()
