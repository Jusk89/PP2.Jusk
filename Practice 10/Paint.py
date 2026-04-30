import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
RED = (220, 50, 50)
GREEN = (50, 200, 50)
BLUE = (50, 50, 220)
YELLOW = (240, 240, 50)

# Canvas for drawing
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

# Current settings
color = BLACK
brush_size = 6
drawing = False
tool = "brush"
start_pos = None

font = pygame.font.SysFont(None, 22)


def draw_toolbar():
    # Draw toolbar background
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, 60))

    # Draw color buttons
    colors = [BLACK, RED, GREEN, BLUE, YELLOW]
    for i, c in enumerate(colors):
        pygame.draw.rect(screen, c, (10 + i * 50, 10, 40, 40))

    # Draw tool buttons
    buttons = [
        ("BRUSH", 270),
        ("RECT", 350),
        ("CIRCLE", 430),
        ("SQUARE", 520),
        ("R TRI", 610),
        ("EQ TRI", 700),
        ("RHOMBUS", 790),
        ("ERASER", 890)
    ]

    for text, x in buttons:
        pygame.draw.rect(screen, (180, 180, 180), (x, 10, 75, 40))
        screen.blit(font.render(text, True, BLACK), (x + 5, 22))

    # Brush size text
    text = font.render(f"SIZE: {brush_size}", True, BLACK)
    screen.blit(text, (10, 65))


def get_square_rect(start, end):
    # Create square from start position to current mouse position
    x1, y1 = start
    x2, y2 = end

    side = min(abs(x2 - x1), abs(y2 - y1))

    if x2 < x1:
        x1 -= side
    if y2 < y1:
        y1 -= side

    return pygame.Rect(x1, y1, side, side)


def get_right_triangle_points(start, end):
    # Points for a right triangle
    x1, y1 = start
    x2, y2 = end

    return [
        (x1, y1),
        (x1, y2),
        (x2, y2)
    ]


def get_equilateral_triangle_points(start, end):
    # Points for an equilateral triangle
    x1, y1 = start
    x2, y2 = end

    side = abs(x2 - x1)
    height = int(side * math.sqrt(3) / 2)

    direction = 1 if y2 > y1 else -1

    return [
        (x1, y1),
        (x1 + side, y1),
        (x1 + side // 2, y1 + direction * height)
    ]


def get_rhombus_points(start, end):
    # Points for a rhombus
    x1, y1 = start
    x2, y2 = end

    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2

    return [
        (center_x, y1),
        (x2, center_y),
        (center_x, y2),
        (x1, center_y)
    ]


def draw_preview():
    # Draw preview before mouse button is released
    if not drawing or start_pos is None:
        return

    end_pos = pygame.mouse.get_pos()

    if tool == "rect":
        x1, y1 = start_pos
        rect = pygame.Rect(x1, y1, end_pos[0] - x1, end_pos[1] - y1)
        rect.normalize()
        pygame.draw.rect(screen, color, rect, 2)

    elif tool == "circle":
        radius = int(math.dist(start_pos, end_pos))
        pygame.draw.circle(screen, color, start_pos, radius, 2)

    elif tool == "square":
        rect = get_square_rect(start_pos, end_pos)
        pygame.draw.rect(screen, color, rect, 2)

    elif tool == "right_triangle":
        points = get_right_triangle_points(start_pos, end_pos)
        pygame.draw.polygon(screen, color, points, 2)

    elif tool == "equilateral_triangle":
        points = get_equilateral_triangle_points(start_pos, end_pos)
        pygame.draw.polygon(screen, color, points, 2)

    elif tool == "rhombus":
        points = get_rhombus_points(start_pos, end_pos)
        pygame.draw.polygon(screen, color, points, 2)


running = True
while running:
    clock.tick(120)
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            # Decrease brush size
            if event.key == pygame.K_LEFTBRACKET:
                brush_size = max(2, brush_size - 1)

            # Increase brush size
            if event.key == pygame.K_RIGHTBRACKET:
                brush_size = min(50, brush_size + 1)

        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # Toolbar buttons
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

                elif 270 < x < 345:
                    tool = "brush"
                elif 350 < x < 425:
                    tool = "rect"
                elif 430 < x < 505:
                    tool = "circle"
                elif 520 < x < 595:
                    tool = "square"
                elif 610 < x < 685:
                    tool = "right_triangle"
                elif 700 < x < 775:
                    tool = "equilateral_triangle"
                elif 790 < x < 865:
                    tool = "rhombus"
                elif 890 < x < 965:
                    tool = "eraser"

            else:
                drawing = True
                start_pos = event.pos

        # Mouse release: draw final shape on canvas
        if event.type == pygame.MOUSEBUTTONUP:
            if drawing and start_pos:
                end_pos = event.pos

                if tool == "rect":
                    x1, y1 = start_pos
                    rect = pygame.Rect(x1, y1, end_pos[0] - x1, end_pos[1] - y1)
                    rect.normalize()
                    pygame.draw.rect(canvas, color, rect, brush_size)

                elif tool == "circle":
                    radius = int(math.dist(start_pos, end_pos))
                    pygame.draw.circle(canvas, color, start_pos, radius, brush_size)

                elif tool == "square":
                    rect = get_square_rect(start_pos, end_pos)
                    pygame.draw.rect(canvas, color, rect, brush_size)

                elif tool == "right_triangle":
                    points = get_right_triangle_points(start_pos, end_pos)
                    pygame.draw.polygon(canvas, color, points, brush_size)

                elif tool == "equilateral_triangle":
                    points = get_equilateral_triangle_points(start_pos, end_pos)
                    pygame.draw.polygon(canvas, color, points, brush_size)

                elif tool == "rhombus":
                    points = get_rhombus_points(start_pos, end_pos)
                    pygame.draw.polygon(canvas, color, points, brush_size)

            drawing = False
            start_pos = None

    # Free drawing with brush or eraser
    if drawing:
        mx, my = pygame.mouse.get_pos()

        if my > 60:
            if tool == "brush":
                pygame.draw.circle(canvas, color, (mx, my), brush_size)

            elif tool == "eraser":
                pygame.draw.circle(canvas, WHITE, (mx, my), brush_size * 3)

    # Draw canvas, preview, and toolbar
    screen.blit(canvas, (0, 0))
    draw_preview()
    draw_toolbar()

    pygame.display.update()

pygame.quit()