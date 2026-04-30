
import pygame
import os
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
surface = pygame.Surface((100, 100), pygame.SRCALPHA)
surface.fill((255, 0, 0, 128))
pygame.display.set_caption("Моё")
x= 50
y= 50
radius = 25
speed = 9
running = True
is_blue= True

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            screen.fill((0, 0, 0))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    key=pygame.key.get_pressed()
    if key[pygame.K_w]:
        if y - radius - speed >= 0:
            y -= speed

    if key[pygame.K_s]:
        if y + radius + speed <= screen.get_height():
            y += speed

    if key[pygame.K_d]:
        if x + radius + speed <= screen.get_width():
            x += speed

    if key[pygame.K_a]:
        if x - radius - speed >= 0:
            x -= speed
    screen.fill((0, 0, 0))

    if is_blue: color = (0, 128, 255)
    else: color = (255, 100, 0)
    pygame.draw.circle(screen, color, (x, y), radius)
    screen.blit(surface, (50, 50))
    clock.tick(60)
    pygame.display.flip()
pygame.quit()