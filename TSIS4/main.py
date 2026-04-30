import pygame
from game import play
from db import get_top_scores

pygame.init()

screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 40)


def text(msg, x, y):
    screen.blit(font.render(msg, True, (255,255,255)), (x,y))


def get_username():
    name = ""

    while True:
        screen.fill((0,0,0))
        text("Enter name:", 200, 120)
        text(name, 200, 180)
        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    return name
                elif e.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += e.unicode


def leaderboard():
    scores = get_top_scores()

    while True:
        screen.fill((0,0,0))
        text("TOP 10", 240, 50)

        for i, s in enumerate(scores):
            text(f"{i+1}. {s[0]} - {s[1]}", 150, 100 + i*30)

        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                return


def menu():
    while True:
        screen.fill((0,0,0))
        text("1 - Play", 230, 120)
        text("2 - Leaderboard", 200, 180)
        text("ESC - Quit", 210, 240)

        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_1:
                    return "play"
                if e.key == pygame.K_2:
                    leaderboard()
                if e.key == pygame.K_ESCAPE:
                    return "quit"


state = "menu"

while state != "quit":
    if state == "menu":
        state = menu()

    elif state == "play":
        user = get_username()
        state = play(screen, clock, user)

pygame.quit()