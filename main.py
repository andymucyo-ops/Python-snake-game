
#imports
from pyfiglet import Figlet
from os import system
from src import game, snake, apple # noqa: F401

#initial game print to welcome the player
welcome_msg: Figlet = Figlet(font = "larry3d",)

print(welcome_msg.renderText("TERMINAL SNAKE GAME"))

input("Press any key to start")

system("clear")


# setup game board

board = game.Game(16,32)

# start game

board.display_print()

board.player_interaction()

