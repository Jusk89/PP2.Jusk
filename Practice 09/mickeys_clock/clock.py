import pygame
from datetime import datetime

# Initialize pygame
pygame.init()

# Window settings
WIDTH = 700
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

# Icon
icon = pygame.image.load("images/micky.jpeg")
pygame.display.set_icon(icon)

# Background
background = pygame.image.load("images/clock.jpeg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Clock hands
right_hand = pygame.image.load("images/right_hand.png")   # minute hand
left_hand = pygame.image.load("images/left_hand.png")     # second hand

# Optional: scale hands if needed
# You can change these sizes depending on your images
right_hand = pygame.transform.scale(right_hand, (50, 300))
left_hand = pygame.transform.scale(left_hand, (40, 350))

# Center of the clock
center_x = WIDTH // 2
center_y = HEIGHT // 2

# Clock for FPS
clock = pygame.time.Clock()

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get current system time
    now = datetime.now()
    minutes = now.minute
    seconds = now.second

    # Convert time to angles
    # 360 degrees / 60 units = 6 degrees per minute/second
    minute_angle = -6 * minutes
    second_angle = -6 * seconds

    # Rotate hands
    rotated_right = pygame.transform.rotate(right_hand, minute_angle)
    rotated_left = pygame.transform.rotate(left_hand, second_angle)

    # Keep rotated hands centered
    right_rect = rotated_right.get_rect(center=(center_x, center_y))
    left_rect = rotated_left.get_rect(center=(center_x, center_y))

    # Draw everything
    screen.blit(background, (0, 0))
    screen.blit(rotated_right, right_rect)
    screen.blit(rotated_left, left_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()