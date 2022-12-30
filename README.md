Copyright 2022 Alexandru Mihai, Maria Sfiraiala, Ioana Tudor, Costin Vlad

# Wordle Bot - Project1

Our Wordle Bot is an improved adaptation of the popular online game [Wordle](https://www.nytimes.com/games/wordle/index.html).
It comes with an automatic gameplay (what we call `AI play`), but also maintains the classic `Wordle` experience both die-hard fans and casual users became to love and appreciate.

We pride ourselves with the performance of our bot (you cannot go wrong when testing the waters with it) and the familiar feeling of the normal gameplay.
Clean contributions on GitHub are another powerfull aspect of our work and we are always ready for new contributors!

## Installation

1. Clone our repository:

   ```console
   $ git clone git@github.com:mariasfiraiala/WordleBot.git
   ```

1. Run the `install.sh` script (for Debian based distros):

   ```console
   $ ./install.sh
   ```

And... you're done!
The setup is ready and the game is running.
You can choose between either letting the bot play for you, or, if you're more confident, guess the words by yourself
Enjoy it!

## Usage

After running the installation script, you'll immediately be prompted to choose between the 2 game scenarios.
If you let the bot play, you'll only be required to press `ENTER` after every completed word.
If you're playing the game yourself, naturally, you'd be more involved.
Type your word of choice; delete letters from it; make sure it's a viable English word, otherwise it won't be accepted; finally, sent the word for validation, using `ENTER`.

## For Developers Only

The structure of the project revolves around the entry point of the app, `start_menu.py`.
From `start_menu.py` the flow divides itself depending on the user's choice: it relies on either `wordle_bot.py` and `wordle_player`.`wordle_player` uses the `grid` module, while the `menu` module was used earlier, by the entry point.
Finally, the `words.py` file is a long, exhaustive list of all 5 letters words in the English language.
