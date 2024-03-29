import pygame

EMPTY,EDGE = 0,0
BLACK = 1
WHITE = -1
WIDTH, HEIGHT = 800, 800
BOARD_COLOR = (0, 180, 0)
RED_COLOR = (255, 0, 0)
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//ROWS
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
PIECE_RADIUS = SQUARE_SIZE // 2 - 5
THETA = 22

board = [
    [      2,     2, EDGE, EDGE, EDGE, EDGE,     2,     2,],
    [      2, EDGE, EMPTY, EMPTY, EMPTY, EMPTY, EDGE,     2,], 
    [  EDGE, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EDGE,], 
    [  EDGE, EMPTY, EMPTY, BLACK, WHITE, EMPTY, EMPTY, EDGE,], 
    [  EDGE, EMPTY, EMPTY, WHITE, BLACK, EMPTY, EMPTY, EDGE,], 
    [  EDGE, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EDGE,], 
    [      2, EDGE, EMPTY, EMPTY, EMPTY, EMPTY, EDGE,     2,],
    [      2,     2, EDGE, EDGE, EDGE, EDGE,     2,     2,],
]
