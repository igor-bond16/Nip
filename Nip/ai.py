from settings import *
import pygame
import time

class AI:
    def __init__(self, win):
        self.win = win
        self.ai = BLACK

    def is_valid_move(self, row, col):
        if board[row][col] != EMPTY:
            return False
        
        if self.is_on_the_edge(row,col):
            flip_row,flip_col = self.determine_direction(row,col)
            while (flip_row != row and flip_col != col) :
                if board[flip_row][flip_col] == EMPTY:
                    break
                elif board[flip_row][flip_col] == -self.ai:
                    flip_row,flip_col = self.determine_direction(flip_row,flip_col)
                    flipped = True
                else:
                    if flipped:
                        return True
                    break

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
        if row == 0 or row == 7 or col == 0 or col == 7:
            return True
        
        for drow in [1,-1]:
            check_row= row + drow
            if check_row == 8 or check_row == -1 or board[check_row][col] == 2:
                return True
        
        for dcol in [1,-1]:
            check_col= col + dcol
            if check_col == 8 or check_col == -1 or board[row][check_col] == 2:
                return True
        
        return False
    
    def determine_direction(self,row,col):
        direction = None
        if self.is_on_the_edge(row,col):

            counter = 0
            for drow in [1,-1]:
                check_row= row + drow
                if check_row == 8 or check_row == -1 or board[check_row][col] == 2 :
                    counter += drow
            
            for dcol in [1,-1]:
                check_col= col + dcol
                if check_col == 8 or check_col == -1 or board[row][check_col] == 2 :
                    counter += dcol
            
            if counter == 2:
                #bottom right
                direction = (drow,dcol) = (-1,-1)
                # print('bottom right')
            elif counter == -2:
                #top left
                direction = (drow,dcol) = (1,1)
                # print('top left')
            elif counter == 0:
                #bottom left
                if row >= 5:
                    direction = (drow,dcol) = (1,-1)
                    # print('bottom left')
                #top right
                elif row <= 2:
                    direction = (drow,dcol) = (-1,1)
                    # print('top right')
            else:
                #left
                if col == 0:
                    direction = (drow,dcol) = (1,0)
                #right
                elif col == 7:
                    direction = (drow,dcol) = (-1,0)
                #top
                elif row == 0:
                    direction = (drow,dcol) = (0,1)
                #bottom
                elif row == 7:
                    direction = (drow,dcol) = (0,-1)


        return direction

    def get_valid_moves(self):
        valid_moves = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.is_valid_move(row, col):
                    valid_moves.append((row, col))
        return valid_moves

    def ai_move(self, board):
        max_captured = 0
        best_move = None
        for row, col in self.get_valid_moves():
            captured = 0
            for drow in [-1, 0, 1]:
                for dcol in [-1, 0, 1]:
                    if drow == 0 and dcol == 0:
                        continue
                    flip_row, flip_col = row + drow, col + dcol
                    while 0 <= flip_row < ROWS and 0 <= flip_col < COLS and board[flip_row][flip_col] == -self.ai:
                        flip_row += drow
                        flip_col += dcol
                        captured += 1

            if captured > max_captured:
                max_captured = captured
                best_move = (row, col)

        if best_move is not None:
            row, col = best_move
            board[row][col] = self.ai
            pygame.draw.circle(self.win, BLACK_COLOR, (
                col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), PIECE_RADIUS)
            pygame.display.update()
            time.sleep(0.3)
            for drow in [-1, 0, 1]:
                for dcol in [-1, 0, 1]:
                    if drow == 0 and dcol == 0:
                        continue
                    flip_row, flip_col = row + drow, col + dcol
                    flipped = False
                    while 0 <= flip_row < ROWS and 0 <= flip_col < COLS and board[flip_row][flip_col] == -self.ai:
                        flip_row += drow
                        flip_col += dcol
                        flipped = True
                    if flipped:
                        flip_row, flip_col = row + drow, col + dcol
                        while 0 <= flip_row < ROWS and 0 <= flip_col < COLS and board[flip_row][flip_col] == -self.ai:
                            board[flip_row][flip_col] = self.ai
                            pygame.draw.circle(self.win, BLACK_COLOR, (
                                flip_col*SQUARE_SIZE + SQUARE_SIZE // 2, flip_row*SQUARE_SIZE + SQUARE_SIZE // 2), PIECE_RADIUS)