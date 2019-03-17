import pygame

pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Adventure Game")

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    controls = pygame.key.get_pressed()
    screenWidth = 500
    screenLength = 500
    if controls[pygame.K_RIGHT] and x < screenWidth - width - vel:
        x += vel
    if controls[pygame.K_LEFT] and x > vel:
        x -= vel
    if controls[pygame.K_UP] and y > vel:
        y -= vel
    if controls[pygame.K_DOWN] and y < screenLength - height - vel:
        y += vel

    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 255, 255), (x, y, width, height))
    pygame.display.update()
pygame.quit()
