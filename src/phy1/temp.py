#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame
import sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500), 0, 32)

# Special Flags
special_flags_list = [0, pygame.BLEND_ADD, pygame.BLEND_SUB, pygame.BLEND_MULT, pygame.BLEND_MIN, pygame.BLEND_MAX,
                      pygame.BLEND_RGB_ADD, pygame.BLEND_RGB_SUB,-1]
print(special_flags_list[1])
# Loop ------------------------------------------------------- #
while True:
    # Background --------------------------------------------- #
    screen.fill((100, 10, 10))

    # Draw circles with different special flags
    for i, flag in enumerate(special_flags_list):
        x = 50 + i * 40
        y = 250
        radius = 20
        color = (255, 255, 255)
        pygame.draw.circle(screen, color, (x, y), radius)
        if flag!=-1:
            # Draw a surface with special flags on each circle
            circle_surf = pygame.Surface((radius * 2+8, radius * 2+8), flags=pygame.SRCALPHA)
            pygame.draw.circle(circle_surf, (20,20,20), (radius+4, 4+radius), radius+4)
            circle_surf.set_colorkey((0, 0, 0))
            # circle_surf.set_alpha(100)  # Adjust transparency for better visualization
            screen.blit(circle_surf, (x - radius-4, y - radius-4), special_flags=flag)

    # Buttons ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Update ------------------------------------------------- #
    pygame.display.update()
    mainClock.tick(60)
