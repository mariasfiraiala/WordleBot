"""
    Wordle Bot is a script that provides both automatic and live Wordle gameplays.
"""

import sys
import pygame
from infrastructure import grid

while True:
    if grid.game_result != "":
        grid.play_again()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if grid.game_result != "":
                    grid.reset()
                else:
                    if len(grid.current_guess_string) == 5 and grid.current_guess_string.lower() in grid.WORDS:
                        grid.check_guess(grid.current_guess)
            elif event.key == pygame.K_BACKSPACE:
                if len(grid.current_guess_string) > 0:
                    grid.delete_letter()
            else:
                key_pressed = event.unicode.upper()
                if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                    if len(grid.current_guess_string) < 5:
                        grid.create_new_letter(key_pressed)
