import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
RED = (220, 50, 50)
GREEN = (50, 200, 50)
BLUE = (50, 50, 220)
YELLOW = (240, 240, 50)

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

color = BLACK
brush_size = 6
drawing = False
tool = "brush"
start_pos = None

font = pygame.font.SysFont(None, 24)

def draw_toolbar():
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, 60))

    colors = [BLACK, RED, GREEN, BLUE, YELLOW]
    for i, c in enumerate(colors):
        pygame.draw.rect(screen, c, (10 + i * 50, 10, 40, 40))

    pygame.draw.rect(screen, (180, 180, 180), (270, 10, 80, 40))
    screen.blit(font.render("BRUSH", True, BLACK), (280, 20))

    pygame.draw.rect(screen, (180, 180, 180), (360, 10, 80, 40))
    screen.blit(font.render("RECT", True, BLACK), (375, 20))

    pygame.draw.rect(screen, (180, 180, 180), (450, 10, 80, 40))
    screen.blit(font.render("CIRCLE", True, BLACK), (460, 20))

    pygame.draw.rect(screen, WHITE, (540, 10, 80, 40))
    screen.blit(font.render("ERASER", True, BLACK), (545, 20))

    pygame.draw.rect(screen, (150, 150, 150), (630, 10, 80, 40))
    screen.blit(font.render("CLEAR", True, BLACK), (640, 20))

    text = font.render(f"SIZE: {brush_size}", True, BLACK)
    screen.blit(text, (730, 20))

def draw_preview():
    if not drawing or start_pos is None:
        return

    mx, my = pygame.mouse.get_pos()

    if tool == "rect":
        x1, y1 = start_pos
        rect = pygame.Rect(x1, y1, mx - x1, my - y1)
        rect.normalize()
        pygame.draw.rect(screen, color, rect, 2)

    elif tool == "circle":
        radius = int(math.dist(start_pos, (mx, my)))
        pygame.draw.circle(screen, color, start_pos, radius, 2)

running = True
while running:
    clock.tick(120)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_LEFTBRACKET:
                brush_size = max(2, brush_size - 1)

            if event.key == pygame.K_RIGHTBRACKET:
                brush_size = min(50, brush_size + 1)

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            if y < 60:
                if 10 < x < 50:
                    color = BLACK
                    tool = "brush"
                elif 60 < x < 100:
                    color = RED
                    tool = "brush"
                elif 110 < x < 150:
                    color = GREEN
                    tool = "brush"
                elif 160 < x < 200:
                    color = BLUE
                    tool = "brush"
                elif 210 < x < 250:
                    color = YELLOW
                    tool = "brush"

                elif 270 < x < 350:
                    tool = "brush"

                elif 360 < x < 440:
                    tool = "rect"

                elif 450 < x < 530:
                    tool = "circle"

                elif 540 < x < 620:
                    tool = "eraser"

                elif 630 < x < 710:
                    canvas.fill(WHITE)

            else:
                drawing = True
                start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if drawing and start_pos:
                end_pos = event.pos

                if tool == "rect":
                    x1, y1 = start_pos
                    x2, y2 = end_pos

                    rect = pygame.Rect(x1, y1, x2 - x1, y2 - y1)
                    rect.normalize()

                    pygame.draw.rect(canvas, color, rect, brush_size)

                elif tool == "circle":
                    radius = int(math.dist(start_pos, end_pos))
                    pygame.draw.circle(canvas, color, start_pos, radius, brush_size)

            drawing = False
            start_pos = None

    if drawing:
        mx, my = pygame.mouse.get_pos()

        if my > 60:
            if tool == "brush":
                pygame.draw.circle(canvas, color, (mx, my), brush_size)

            elif tool == "eraser":
                pygame.draw.circle(canvas, WHITE, (mx, my), brush_size * 3)

    screen.blit(canvas, (0, 0))
    draw_preview()
    draw_toolbar()

    pygame.display.update()

pygame.quit()