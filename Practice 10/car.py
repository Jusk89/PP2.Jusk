import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Race")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GRAY = (40, 40, 40)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
GREEN = (0, 200, 0)

ROAD_LEFT = 50
ROAD_WIDTH = 300

lane_width = ROAD_WIDTH // 3
lanes = [
    ROAD_LEFT + lane_width // 2 - 25,
    ROAD_LEFT + lane_width + lane_width // 2 - 25,
    ROAD_LEFT + lane_width * 2 + lane_width // 2 - 25
]

player_width = 50
player_height = 90
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 120
player_speed = 6

traffic = []
for i in range(3):
    lane = random.randint(0, 2)
    x = lanes[lane]
    y = random.randint(-600, -100)
    speed = random.randint(4, 7)
    traffic.append([lane, x, y, speed])

coins = []
for i in range(5):
    x = random.randint(ROAD_LEFT, ROAD_LEFT + ROAD_WIDTH - 30)
    y = random.randint(-600, -50)
    coins.append([x, y])

score = 0
font = pygame.font.SysFont(None, 36)

running = True
while running:
    clock.tick(60)
    screen.fill(GRAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed

    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    player_x = max(ROAD_LEFT, min(player_x, ROAD_LEFT + ROAD_WIDTH - player_width))

    pygame.draw.rect(screen, (60, 60, 60), (ROAD_LEFT, 0, ROAD_WIDTH, HEIGHT))

    for x in [ROAD_LEFT + lane_width, ROAD_LEFT + lane_width * 2]:
        for y in range(0, HEIGHT, 40):
            pygame.draw.rect(screen, WHITE, (x, y, 4, 20))

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    pygame.draw.rect(screen, RED, player_rect)

    for coin in coins:
        coin_rect = pygame.Rect(coin[0], coin[1], 30, 30)
        pygame.draw.circle(screen, (255, 215, 0), (coin[0] + 15, coin[1] + 15), 15)

        coin[1] += 4

        if coin[1] > HEIGHT:
            coin[0] = random.randint(ROAD_LEFT, ROAD_LEFT + ROAD_WIDTH - 30)
            coin[1] = random.randint(-600, -50)

        if player_rect.colliderect(coin_rect):
            score += 1
            coin[0] = random.randint(ROAD_LEFT, ROAD_LEFT + ROAD_WIDTH - 30)
            coin[1] = random.randint(-600, -50)

    for car in traffic:
        lane, x, y, speed = car

        car_rect = pygame.Rect(x, y, 50, 70)
        pygame.draw.rect(screen, BLUE, car_rect)

        car[2] += speed

        if car[2] > HEIGHT:
            car[0] = random.randint(0, 2)
            car[1] = lanes[car[0]]
            car[2] = random.randint(-300, -100)
            car[3] = random.randint(4, 5)

        if player_rect.colliderect(car_rect):
            print("Game Over! Score:", score)
            running = False

    text = font.render(f"Score: {score}", True, GREEN)
    screen.blit(text, (10, 10))

    pygame.display.update()

pygame.quit()