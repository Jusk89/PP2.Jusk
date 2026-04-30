import pygame
import random
from persistence import save_score
from ui import draw_text

WIDTH, HEIGHT = 500, 700

WHITE = (255, 255, 255)
GRAY = (45, 45, 45)
ROAD = (65, 65, 65)
BLACK = (0, 0, 0)
RED = (220, 40, 40)
BLUE = (40, 80, 220)
GREEN = (40, 200, 80)
YELLOW = (240, 220, 50)
ORANGE = (255, 150, 40)
PURPLE = (170, 70, 220)

ROAD_LEFT = 70
ROAD_WIDTH = 360
LANE_COUNT = 3
LANE_WIDTH = ROAD_WIDTH // LANE_COUNT

lanes = [
    ROAD_LEFT + LANE_WIDTH // 2 - 25,
    ROAD_LEFT + LANE_WIDTH + LANE_WIDTH // 2 - 25,
    ROAD_LEFT + LANE_WIDTH * 2 + LANE_WIDTH // 2 - 25
]

car_colors = {
    "red": RED,
    "blue": BLUE,
    "green": GREEN
}


def get_difficulty_speed(settings):
    if settings["difficulty"] == "easy":
        return 4
    if settings["difficulty"] == "hard":
        return 8
    return 6


def create_enemy():
    lane = random.randint(0, 2)

    return {
        "lane": lane,
        "x": lanes[lane],
        "y": random.randint(-600, -120),
        "speed": random.randint(4, 7)
    }


def create_obstacle():
    lane = random.randint(0, 2)

    return {
        "lane": lane,
        "x": lanes[lane],
        "y": random.randint(-900, -150),
        "kind": random.choice(["oil", "barrier", "slow"])
    }


def create_powerup():
    lane = random.randint(0, 2)

    return {
        "lane": lane,
        "x": lanes[lane] + 10,
        "y": random.randint(-1200, -300),
        "kind": random.choice(["nitro", "shield", "repair"])
    }


def create_coin():
    return {
        "x": random.randint(ROAD_LEFT, ROAD_LEFT + ROAD_WIDTH - 25),
        "y": random.randint(-700, -50),
        "value": random.choice([1, 2, 3])
    }


def game_over_screen(screen, clock, name, score, distance, coins):
    save_score(name, score, distance)

    retry_button = pygame.Rect(150, 390, 200, 55)
    menu_button = pygame.Rect(150, 460, 200, 55)

    while True:
        clock.tick(60)
        screen.fill(BLACK)

        draw_text(screen, "GAME OVER", 155, 120)
        draw_text(screen, f"Score: {score}", 170, 210)
        draw_text(screen, f"Distance: {int(distance)}", 170, 250)
        draw_text(screen, f"Coins: {coins}", 170, 290)

        pygame.draw.rect(screen, GRAY, retry_button)
        pygame.draw.rect(screen, WHITE, retry_button, 2)
        draw_text(screen, "RETRY", 205, 407, WHITE, True)

        pygame.draw.rect(screen, GRAY, menu_button)
        pygame.draw.rect(screen, WHITE, menu_button, 2)
        draw_text(screen, "MAIN MENU", 185, 477, WHITE, True)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_button.collidepoint(event.pos):
                    return "play"

                if menu_button.collidepoint(event.pos):
                    return "menu"


def play_game(screen, clock, name, settings):
    player_w = 50
    player_h = 90
    player_x = lanes[1]
    player_y = HEIGHT - 120
    player_speed = 7

    base_speed = get_difficulty_speed(settings)

    enemies = [create_enemy() for _ in range(3)]
    obstacles = [create_obstacle() for _ in range(3)]
    powerups = [create_powerup() for _ in range(2)]
    coins = [create_coin() for _ in range(5)]

    score = 0
    coins_count = 0
    distance = 0
    finish_distance = 3000

    shield = False
    active_power = None
    power_timer = 0

    while True:
        clock.tick(60)
        screen.fill(GRAY)

        difficulty_bonus = int(distance // 600)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu"

        keys = pygame.key.get_pressed()

        current_player_speed = player_speed
        if active_power == "nitro":
            current_player_speed += 5

        if keys[pygame.K_LEFT]:
            player_x -= current_player_speed

        if keys[pygame.K_RIGHT]:
            player_x += current_player_speed

        player_x = max(ROAD_LEFT, min(player_x, ROAD_LEFT + ROAD_WIDTH - player_w))

        distance += 0.4 + difficulty_bonus * 0.05
        score = coins_count * 10 + int(distance)

        if active_power:
            power_timer -= 1
            if power_timer <= 0:
                active_power = None

        pygame.draw.rect(screen, ROAD, (ROAD_LEFT, 0, ROAD_WIDTH, HEIGHT))

        for x in [ROAD_LEFT + LANE_WIDTH, ROAD_LEFT + LANE_WIDTH * 2]:
            for y in range(0, HEIGHT, 40):
                pygame.draw.rect(screen, WHITE, (x, y, 4, 20))

        player_rect = pygame.Rect(player_x, player_y, player_w, player_h)
        pygame.draw.rect(screen, car_colors[settings["car_color"]], player_rect)

        if shield:
            pygame.draw.circle(screen, BLUE, player_rect.center, 55, 3)

        for coin in coins:
            coin_rect = pygame.Rect(coin["x"], coin["y"], 25, 25)
            pygame.draw.circle(screen, YELLOW, (coin["x"] + 12, coin["y"] + 12), 12)

            coin["y"] += base_speed

            if coin["y"] > HEIGHT:
                coin.update(create_coin())

            if player_rect.colliderect(coin_rect):
                coins_count += coin["value"]
                coin.update(create_coin())

        for enemy in enemies:
            enemy_rect = pygame.Rect(enemy["x"], enemy["y"], 50, 80)
            pygame.draw.rect(screen, BLUE, enemy_rect)

            enemy["y"] += enemy["speed"] + difficulty_bonus

            if enemy["y"] > HEIGHT:
                enemy.update(create_enemy())

            if player_rect.colliderect(enemy_rect):
                if shield:
                    shield = False
                    enemy.update(create_enemy())
                else:
                    return game_over_screen(screen, clock, name, score, distance, coins_count)

        for obstacle in obstacles:
            obstacle_rect = pygame.Rect(obstacle["x"], obstacle["y"], 50, 45)

            if obstacle["kind"] == "oil":
                pygame.draw.ellipse(screen, BLACK, obstacle_rect)
            elif obstacle["kind"] == "barrier":
                pygame.draw.rect(screen, ORANGE, obstacle_rect)
            elif obstacle["kind"] == "slow":
                pygame.draw.rect(screen, PURPLE, obstacle_rect)

            obstacle["y"] += base_speed + difficulty_bonus

            if obstacle["y"] > HEIGHT:
                obstacle.update(create_obstacle())

            if player_rect.colliderect(obstacle_rect):
                if obstacle["kind"] == "slow":
                    player_speed = max(4, player_speed - 1)
                    obstacle.update(create_obstacle())

                elif shield:
                    shield = False
                    obstacle.update(create_obstacle())

                else:
                    return game_over_screen(screen, clock, name, score, distance, coins_count)

        for power in powerups:
            power_rect = pygame.Rect(power["x"], power["y"], 30, 30)

            if power["kind"] == "nitro":
                pygame.draw.rect(screen, GREEN, power_rect)
            elif power["kind"] == "shield":
                pygame.draw.circle(screen, BLUE, power_rect.center, 16)
            elif power["kind"] == "repair":
                pygame.draw.rect(screen, RED, power_rect)

            power["y"] += base_speed

            if power["y"] > HEIGHT:
                power.update(create_powerup())

            if player_rect.colliderect(power_rect):
                if power["kind"] == "nitro":
                    active_power = "nitro"
                    power_timer = 240

                elif power["kind"] == "shield":
                    active_power = "shield"
                    shield = True
                    power_timer = 999999

                elif power["kind"] == "repair":
                    player_speed = 7

                power.update(create_powerup())

        if random.randint(1, 500) == 1:
            obstacles.append(create_obstacle())

        draw_text(screen, f"Score: {score}", 10, 10, GREEN, True)
        draw_text(screen, f"Coins: {coins_count}", 10, 35, GREEN, True)
        draw_text(screen, f"Distance: {int(distance)}/{finish_distance}", 10, 60, GREEN, True)

        if active_power == "nitro":
            draw_text(screen, f"Power: Nitro {power_timer // 60}s", 300, 10, YELLOW, True)

        elif active_power == "shield":
            draw_text(screen, "Power: Shield", 300, 10, YELLOW, True)

        pygame.display.update()

        if distance >= finish_distance:
            return game_over_screen(screen, clock, name, score + 1000, distance, coins_count)