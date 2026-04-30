import pygame
from racer import play_game
from ui import draw_text, draw_button
from persistence import load_json, save_json, SETTINGS_FILE, LEADERBOARD_FILE

pygame.init()

WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

settings = load_json(SETTINGS_FILE, {
    "sound": True,
    "car_color": "red",
    "difficulty": "normal"
})


def menu_screen():
    play_btn = pygame.Rect(150, 220, 200, 55)
    leaderboard_btn = pygame.Rect(150, 290, 200, 55)
    settings_btn = pygame.Rect(150, 360, 200, 55)
    quit_btn = pygame.Rect(150, 430, 200, 55)

    while True:
        clock.tick(60)
        screen.fill(BLACK)

        draw_text(screen, "RACER", 190, 120)
        draw_button(screen, "PLAY", play_btn)
        draw_button(screen, "LEADERBOARD", leaderboard_btn)
        draw_button(screen, "SETTINGS", settings_btn)
        draw_button(screen, "QUIT", quit_btn)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_btn.collidepoint(event.pos):
                    return "play"
                if leaderboard_btn.collidepoint(event.pos):
                    return "leaderboard"
                if settings_btn.collidepoint(event.pos):
                    return "settings"
                if quit_btn.collidepoint(event.pos):
                    return "quit"


def username_screen():
    name = ""

    while True:
        clock.tick(60)
        screen.fill(BLACK)

        draw_text(screen, "Enter your name:", 130, 230)
        draw_text(screen, name, 190, 300)
        draw_text(screen, "Press Enter to start", 140, 380, WHITE, True)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name != "":
                    return name

                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]

                elif len(name) < 10:
                    name += event.unicode


def leaderboard_screen():
    leaderboard = load_json(LEADERBOARD_FILE, [])
    back_btn = pygame.Rect(150, 600, 200, 55)

    while True:
        clock.tick(60)
        screen.fill(BLACK)

        draw_text(screen, "TOP 10", 200, 60)

        for i, item in enumerate(leaderboard[:10]):
            text = f"{i + 1}. {item['name']} | Score: {item['score']} | Dist: {item['distance']}"
            draw_text(screen, text, 50, 120 + i * 40, WHITE, True)

        draw_button(screen, "BACK", back_btn)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn.collidepoint(event.pos):
                    return "menu"


def settings_screen():
    global settings

    back_btn = pygame.Rect(150, 580, 200, 55)

    while True:
        clock.tick(60)
        screen.fill(BLACK)

        draw_text(screen, "SETTINGS", 180, 70)
        draw_text(screen, f"Sound: {settings['sound']}", 120, 170)
        draw_text(screen, f"Car color: {settings['car_color']}", 120, 230)
        draw_text(screen, f"Difficulty: {settings['difficulty']}", 120, 290)

        draw_text(screen, "Press S - sound", 120, 380, WHITE, True)
        draw_text(screen, "Press C - car color", 120, 410, WHITE, True)
        draw_text(screen, "Press D - difficulty", 120, 440, WHITE, True)

        draw_button(screen, "BACK", back_btn)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    settings["sound"] = not settings["sound"]

                elif event.key == pygame.K_c:
                    colors = ["red", "blue", "green"]
                    index = colors.index(settings["car_color"])
                    settings["car_color"] = colors[(index + 1) % len(colors)]

                elif event.key == pygame.K_d:
                    levels = ["easy", "normal", "hard"]
                    index = levels.index(settings["difficulty"])
                    settings["difficulty"] = levels[(index + 1) % len(levels)]

                save_json(SETTINGS_FILE, settings)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn.collidepoint(event.pos):
                    return "menu"


state = "menu"

while state != "quit":
    if state == "menu":
        state = menu_screen()

    elif state == "play":
        username = username_screen()

        if username is None:
            state = "quit"
        else:
            state = play_game(screen, clock, username, settings)

    elif state == "leaderboard":
        state = leaderboard_screen()

    elif state == "settings":
        state = settings_screen()

pygame.quit()