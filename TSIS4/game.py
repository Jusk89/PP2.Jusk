import pygame
import random
from config import *
from db import save_score

pygame.init()

font = pygame.font.SysFont(None, 25)


def draw_text(screen, text, x, y):
    img = font.render(text, True, BLACK)
    screen.blit(img, (x, y))


def spawn_food():
    return [
        random.randrange(0, WIDTH, BLOCK),
        random.randrange(0, HEIGHT, BLOCK)
    ]


def spawn_poison():
    return [
        random.randrange(0, WIDTH, BLOCK),
        random.randrange(0, HEIGHT, BLOCK)
    ]


def play(screen, clock, username):
    x = WIDTH // 2
    y = HEIGHT // 2

    dx = 0
    dy = 0

    snake = []
    length = 1

    food = spawn_food()
    poison = spawn_poison()

    score = 0
    level = 1

    speed = 10

    shield = False

    running = True
    game_over = False

    while running:

        while game_over:
            screen.fill(RED)
            draw_text(screen, "Game Over (R - retry / Q - quit)", 150, 180)
            pygame.display.update()

            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_r:
                        return "retry"
                    if e.key == pygame.K_q:
                        return "menu"

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return "quit"

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    dx, dy = -BLOCK, 0
                if e.key == pygame.K_RIGHT:
                    dx, dy = BLOCK, 0
                if e.key == pygame.K_UP:
                    dx, dy = 0, -BLOCK
                if e.key == pygame.K_DOWN:
                    dx, dy = 0, BLOCK

        x += dx
        y += dy

        # Wall collision
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            if shield:
                shield = False
            else:
                game_over = True

        screen.fill(WHITE)

        # Draw food
        pygame.draw.rect(screen, GREEN, (*food, BLOCK, BLOCK))

        # Draw poison
        pygame.draw.rect(screen, PURPLE, (*poison, BLOCK, BLOCK))

        head = [x, y]
        snake.append(head)

        if len(snake) > length:
            del snake[0]

        # Self collision
        for s in snake[:-1]:
            if s == head:
                if shield:
                    shield = False
                else:
                    game_over = True

        # Eat food
        if head == food:
            food = spawn_food()
            length += 1
            score += 10

        # Eat poison
        if head == poison:
            poison = spawn_poison()
            length -= 2

            if length <= 1:
                game_over = True

        # Level up
        if score and score % 50 == 0:
            level += 1
            speed += 2

        # Draw snake
        for s in snake:
            pygame.draw.rect(screen, BLACK, (*s, BLOCK, BLOCK))

        draw_text(screen, f"Score: {score}", 10, 10)
        draw_text(screen, f"Level: {level}", 10, 30)

        pygame.display.update()
        clock.tick(speed)

    save_score(username, score, level)
    return "menu"