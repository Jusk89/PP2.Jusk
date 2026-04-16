import pygame
from datetime import datetime
import math

pygame.init()

WIDTH = 700
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

icon = pygame.image.load("images/micky.jpeg")
pygame.display.set_icon(icon)

background = pygame.image.load("images/clock.jpeg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

right_hand = pygame.image.load("images/right_hand.png").convert_alpha()
left_hand = pygame.image.load("images/left_hand.png").convert_alpha()

right_hand = pygame.transform.smoothscale(right_hand, (40, 220))
left_hand = pygame.transform.smoothscale(left_hand, (35, 260))

center_x = WIDTH // 2
center_y = HEIGHT // 2
clock_center = (center_x, center_y)

clock = pygame.time.Clock()


def draw_hand(surface, image, angle, pivot, offset):
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_offset = offset.rotate(-angle)
    rect = rotated_image.get_rect(center=(pivot[0] + rotated_offset.x,
                                          pivot[1] + rotated_offset.y))
    surface.blit(rotated_image, rect)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.now()
    minutes = now.minute
    seconds = now.second

    minute_angle = -(minutes * 6)
    second_angle = -(seconds * 6)

    screen.blit(background, (0, 0))

    # offset показывает, где будет центр картинки руки
    # подбирай числа, если нужно
    draw_hand(screen, right_hand, minute_angle, clock_center, pygame.math.Vector2(0, -70))
    draw_hand(screen, left_hand, second_angle, clock_center, pygame.math.Vector2(0, -90))

    pygame.display.update()
    clock.tick(60)

pygame.quit()