import pygame
from player import MusicPlayer

pygame.init()

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font_title = pygame.font.SysFont("Arial", 36)
font_text = pygame.font.SysFont("Arial", 28)
font_small = pygame.font.SysFont("Arial", 22)

clock = pygame.time.Clock()

player = MusicPlayer()

running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()

            elif event.key == pygame.K_s:
                player.stop()

            elif event.key == pygame.K_n:
                player.next_track()

            elif event.key == pygame.K_b:
                player.previous_track()

            elif event.key == pygame.K_q:
                running = False

    title_surface = font_title.render("Interactive Music Player", True, (255, 255, 255))
    track_surface = font_text.render(f"Current track: {player.get_current_track_name()}", True, (200, 200, 0))
    pos_surface = font_text.render(f"Position: {player.get_position()} sec", True, (0, 200, 200))

    controls1 = font_small.render("P = Play | S = Stop | N = Next | B = Previous | Q = Quit", True, (180, 180, 180))

    screen.blit(title_surface, (200, 40))
    screen.blit(track_surface, (180, 140))
    screen.blit(pos_surface, (180, 190))
    screen.blit(controls1, (100, 300))

    pygame.display.update()
    clock.tick(30)

pygame.quit()