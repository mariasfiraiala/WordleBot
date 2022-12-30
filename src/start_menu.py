import pygame
import sys
from infrastructure import menu

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    menu.button1.draw()
    menu.button2.draw()

    pygame.display.update()
