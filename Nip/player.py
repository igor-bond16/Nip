import pygame
from settings import *
import time


class Player:
    def __init__(self, win):
        self.win = win
        self.player = WHITE

    def is_valid_move(self, row, col):
        if board[row][col] != EMPTY:
            return False
        
        if self.is_on_the_edge(row,col):
            for drow in [-1, 0, 1]:
                for dcol in [-1, 0, 1]:
                    if drow == 0 and dcol == 0 or board[drow][dcol] == 2 or self.is_on_the_edge(drow,dcol):
                        continue
                    flip_row, flip_col = row + drow, col + dcol
                    flipped = False
                    while 0 <= flip_row < ROWS and 0 <= flip_col < COLS:
                        if board[flip_row][flip_col] == EMPTY:
                            break
                        elif board[flip_row][flip_col] == -self.ai:
                            flip_row += drow
                            flip_col += dcol
                            flipped = True
                        else:
                            if flipped:
                                return True
                            break
                        
            flip_row,flip_col = self.determine_direction(row,col)
            while 0 <= flip_row < ROWS and 0 <= flip_col < COLS:
                if board[flip_row][flip_col] == EMPTY:
                    break
                elif board[flip_row][flip_col] == -self.ai:
                    flip_row,flip_col = self.determine_direction(flip_row,flip_col)
                    flipped = True
                else:
                    if flipped:
                        return True
                    break


        else:
            for drow in [-1, 0, 1]:
                for dcol in [-1, 0, 1]:
                    if drow == 0 and dcol == 0:
                        continue
                    flip_row, flip_col = row + drow, col + dcol
                    flipped = False
                    while 0 <= flip_row < ROWS and 0 <= flip_col < COLS:
                        if board[flip_row][flip_col] == EMPTY:
                            break
                        elif board[flip_row][flip_col] == -self.ai:
                            flip_row += drow
                            flip_col += dcol
                            flipped = True
                        else:
                            if flipped:
                                return True
                            break
        return False
    
    def is_on_the_edge(self,row,col):
        for drow in [-1, 0, 1]:
            for dcol in [-1, 0, 1]:
                if drow == 0 and dcol == 0:
                    continue
                check_row, check_col = row + drow, col + dcol
                if board[check_row][check_col] == 2:
                    return True
                else:
                    continue
        return False

    def get_valid_moves(self):
        valid_moves = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.is_valid_move(row, col):
                    valid_moves.append((row, col))
        return valid_moves

    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            board[row][col] = self.player
            pygame.draw.circle(self.win, WHITE_COLOR, (col*SQUARE_SIZE +
                               SQUARE_SIZE // 2, row*SQUARE_SIZE + SQUARE_SIZE // 2), PIECE_RADIUS)
            pygame.display.update()
            time.sleep(0.3)
            for drow in [-1, 0, 1]:
                for dcol in [-1, 0, 1]:
                    if drow == 0 and dcol == 0:
                        continue
                    flip_row, flip_col = row + drow, col + dcol
                    flipped = False
                    while flip_row >= 0 and flip_row < ROWS and flip_col >= 0 and flip_col < COLS:
                        if board[flip_row][flip_col] == EMPTY:
                            break
                        elif board[flip_row][flip_col] == -self.player:
                            flip_row += drow
                            flip_col += dcol
                            flipped = True
                        else:
                            if flipped:
                                while True:
                                    flip_row -= drow
                                    flip_col -= dcol
                                    board[flip_row][flip_col] = self.player
                                    pygame.draw.circle(self.win, WHITE_COLOR, (
                                        flip_col*SQUARE_SIZE + SQUARE_SIZE // 2, flip_row*SQUARE_SIZE + SQUARE_SIZE // 2), PIECE_RADIUS)
                                    pygame.display.update()
                                    time.sleep(0.3)
                                    if flip_row == row and flip_col == col:
                                        break
                                break
                            else:
                                break