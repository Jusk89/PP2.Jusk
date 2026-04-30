import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Race")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
GRAY = (40, 40, 40)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
GREEN = (0, 200, 0)
GOLD = (255, 215, 0)
ORANGE = (255, 140, 0)
PURPLE = (160, 32, 240)

# Road settings
ROAD_LEFT = 50
ROAD_WIDTH = 300

lane_width = ROAD_WIDTH // 3
lanes = [
    ROAD_LEFT + lane_width // 2 - 25,
    ROAD_LEFT + lane_width + lane_width // 2 - 25,
    ROAD_LEFT + lane_width * 2 + lane_width // 2 - 25
]

# Player settings
player_width = 50
player_height = 90
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 120
player_speed = 6

# Enemy speed settings
enemy_speed_bonus = 0
coins_collected = 0
N = 5   # Enemy speed increases every 5 collected coins

# Traffic/enemy cars
traffic = []
for i in range(3):
    lane = random.randint(0, 2)
    x = lanes[lane]
    y = random.randint(-600, -100)
    speed = random.randint(4, 7)
    traffic.append([lane, x, y, speed])

# Function for creating a random coin
def create_coin():
    # Different coin types have different values and colors
    coin_types = [
        {"value": 1, "color": GOLD, "radius": 12},
        {"value": 2, "color": ORANGE, "radius": 14},
        {"value": 3, "color": PURPLE, "radius": 16}
    ]

    coin_type = random.choice(coin_types)

    x = random.randint(ROAD_LEFT, ROAD_LEFT + ROAD_WIDTH - 30)
    y = random.randint(-600, -50)

    return [x, y, coin_type["value"], coin_type["color"], coin_type["radius"]]

# Coins list
coins = []
for i in range(5):
    coins.append(create_coin())

score = 0
font = pygame.font.SysFont(None, 36)

running = True
while running:
    clock.tick(60)
    screen.fill(GRAY)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Player movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed

    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Keep player inside the road
    player_x = max(ROAD_LEFT, min(player_x, ROAD_LEFT + ROAD_WIDTH - player_width))

    # Draw road
    pygame.draw.rect(screen, (60, 60, 60), (ROAD_LEFT, 0, ROAD_WIDTH, HEIGHT))

    # Draw lane lines
    for x in [ROAD_LEFT + lane_width, ROAD_LEFT + lane_width * 2]:
        for y in range(0, HEIGHT, 40):
            pygame.draw.rect(screen, WHITE, (x, y, 4, 20))

    # Draw player
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    pygame.draw.rect(screen, RED, player_rect)

    # Update and draw coins
    for coin in coins:
        coin_x, coin_y, coin_value, coin_color, coin_radius = coin

        coin_rect = pygame.Rect(coin_x, coin_y, 30, 30)

        # Draw coin with its own color and size
        pygame.draw.circle(
            screen,
            coin_color,
            (coin_x + 15, coin_y + 15),
            coin_radius
        )

        # Move coin down
        coin[1] += 4

        # Respawn coin if it leaves the screen
        if coin[1] > HEIGHT:
            new_coin = create_coin()
            coin[0] = new_coin[0]
            coin[1] = new_coin[1]
            coin[2] = new_coin[2]
            coin[3] = new_coin[3]
            coin[4] = new_coin[4]

        # Check collision with player
        if player_rect.colliderect(coin_rect):
            score += coin_value
            coins_collected += 1

            # Increase enemy speed every N collected coins
            if coins_collected % N == 0:
                enemy_speed_bonus += 1

            # Respawn collected coin
            new_coin = create_coin()
            coin[0] = new_coin[0]
            coin[1] = new_coin[1]
            coin[2] = new_coin[2]
            coin[3] = new_coin[3]
            coin[4] = new_coin[4]

    # Update and draw enemy cars
    for car in traffic:
        lane, x, y, speed = car

        car_rect = pygame.Rect(x, y, 50, 70)
        pygame.draw.rect(screen, BLUE, car_rect)

        # Enemy speed includes bonus speed
        car[2] += speed + enemy_speed_bonus

        # Respawn enemy car
        if car[2] > HEIGHT:
            car[0] = random.randint(0, 2)
            car[1] = lanes[car[0]]
            car[2] = random.randint(-300, -100)
            car[3] = random.randint(4, 5)

        # Check collision with player
        if player_rect.colliderect(car_rect):
            print("Game Over! Score:", score)
            running = False

    # Draw score and collected coins
    text = font.render(f"Score: {score}", True, GREEN)
    screen.blit(text, (10, 10))

    coin_text = font.render(f"Coins: {coins_collected}", True, GREEN)
    screen.blit(coin_text, (10, 45))

    pygame.display.update()

pygame.quit()