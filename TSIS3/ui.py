import pygame

pygame.font.init()

font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 24)


def draw_text(screen, text, x, y, color):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


def draw_button(screen, rect, text):
    pygame.draw.rect(screen, (70, 70, 70), rect)
    pygame.draw.rect(screen, (255, 255, 255), rect, 2)
    txt = small_font.render(text, True, (255, 255, 255))
    screen.blit(txt, (rect.x + 10, rect.y + 10))