"""
    Wordle Bot is a script that provides automatic Wordle gameplays.
"""

import sys
import pygame
import random
from infrastructure import grid
from words import *

all_words = WORDS

grid.bot_message()

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
                    all_words = WORDS
                    grid.reset()
                    grid.bot_message()
                else:
                    grid.create_new_word(random.choice(all_words))
                    current_string = grid.current_guess_string
                    result = grid.check_guess(grid.current_guess)
                    grid.current_guess_string = current_string
                    # Using the current guess and result to eliminate the other words
                    all_words = grid.update_words(all_words, result)
