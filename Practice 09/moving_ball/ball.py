
import pygame
import os
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
surface = pygame.Surface((100, 100), pygame.SRCALPHA)
surface.fill((255, 0, 0, 128))
pygame.display.set_caption("Моё первое окно")
x= 30
y= 30
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
    if key[pygame.K_w]: y -=9
    if key[pygame.K_s]: y +=9
    if key[pygame.K_d]: x +=9
    if key[pygame.K_a]: x -=9
    screen.fill((0, 0, 0))

    if is_blue: color = (0, 128, 255)
    else: color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 20, 20))
    screen.blit(surface, (50, 50))
    clock.tick(60)
    pygame.display.flip()
pygame.quit()