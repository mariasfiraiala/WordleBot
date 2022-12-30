"""
    Wordle Player is a script that provides live Wordle gameplays.
"""

import sys
import pygame
from infrastructure import grid

grid.player_message()

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
                    grid.player_message()
                else:
                    if len(grid.current_guess_string) == 5:
                        if grid.current_guess_string.lower() in grid.WORDS:
                            result = grid.check_guess(grid.current_guess)
                            grid.good_message()
                        else:
                            grid.bad_message()
            elif event.key == pygame.K_BACKSPACE:
                if len(grid.current_guess_string) > 0:
                    grid.delete_letter()
            else:
                key_pressed = event.unicode.upper()
                if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                    if len(grid.current_guess_string) < 5:
                        grid.create_new_letter(key_pressed)
