import pygame

pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (60, 60, 60)

font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 24)


def draw_text(screen, text, x, y, color=WHITE, small=False):
    used_font = small_font if small else font
    image = used_font.render(text, True, color)
    screen.blit(image, (x, y))


def draw_button(screen, text, rect):
    pygame.draw.rect(screen, GRAY, rect)
    pygame.draw.rect(screen, WHITE, rect, 2)
    draw_text(screen, text, rect.x + 20, rect.y + 13, WHITE, True)