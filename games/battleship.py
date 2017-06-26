"""Play battleship!"""
import numpy as np


"""
- global variables hold the game state
- interface is what?
    * game_in_progress flag (use a while loop to play)
    * report_move
    * get_picture
    * print state (can play in terminal)
- locally need what functions?
    * layout_ships
"""


GAME_IN_PROGRESS = False
BOT_BOATS = np.zeros((4, 4), 'int32')
USR_BOATS = np.zeros((4, 4), 'int32')
BOT_SHOTS = np.zeros((4, 4), 'int32')
USR_SHOTS = np.zeros((4, 4), 'int32')


class Orientation:
    Up, Right, Down, Left = np.arange(4)


def init():
    global BOT_BOATS, USR_BOATS, BOT_SHOTS, USR_SHOTS
    BOT_BOATS = np.zeros((4, 4), 'int32')
    USR_BOATS = np.zeros((4, 4), 'int32')
    BOT_SHOTS = np.zeros((4, 4), 'int32')
    USR_SHOTS = np.zeros((4, 4), 'int32')


def place_ship(board, length):
    """Plan:

    Randomly select a square.
    Randomly select an orientation.
    Check if the orientation crosses the boundary.
    If crossing, try another orientation.
    If all orientations fail, randomly pick another square.
    """
    square = np.argmax(np.random.rand(16))
    while True:
        # convert the number to a square in the matrix
