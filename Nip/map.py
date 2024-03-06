from settings import *
import pygame,math

class Map:
    def __init__(self,win):
        self.win = win

    def draw(self):
        self.win.fill(BOARD_COLOR)

        pygame.draw.line(
            self.win, BLACK_COLOR, (5 * SQUARE_SIZE + SQUARE_SIZE // 2, SQUARE_SIZE // 2), (7 * SQUARE_SIZE + SQUARE_SIZE // 2, 2*SQUARE_SIZE + SQUARE_SIZE // 2), 3)
        pygame.draw.line(
            self.win, BLACK_COLOR, (SQUARE_SIZE // 2, 2*SQUARE_SIZE + SQUARE_SIZE // 2), (2 * SQUARE_SIZE + SQUARE_SIZE // 2, SQUARE_SIZE // 2), 3)
        pygame.draw.line(
            self.win, BLACK_COLOR, (SQUARE_SIZE // 2, 5*SQUARE_SIZE + SQUARE_SIZE // 2), (2*SQUARE_SIZE + SQUARE_SIZE // 2, 7*SQUARE_SIZE + SQUARE_SIZE // 2), 3)
        pygame.draw.line(
            self.win, BLACK_COLOR, (5*SQUARE_SIZE + SQUARE_SIZE // 2, 7*SQUARE_SIZE + SQUARE_SIZE // 2), (7*SQUARE_SIZE + SQUARE_SIZE // 2, 5*SQUARE_SIZE + SQUARE_SIZE // 2), 3)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] != 2 :
                    
                    x = col * SQUARE_SIZE + SQUARE_SIZE // 2 
                    y = row * SQUARE_SIZE + SQUARE_SIZE // 2

                    # Draw the cell
                    pygame.draw.circle(self.win, WHITE_COLOR, (x, y), PIECE_RADIUS//3, 2)
                    if col < COLS - 1 and not (board[row][col + 1] == 2):
                        x2 = x + SQUARE_SIZE
                        y2 = y
                        pygame.draw.line(self.win, BLACK_COLOR, (x, y), (x2, y2), 3)

                    # Draw the vertical line below the cell
                    if row < ROWS - 1 and not (board[row+1][col] == 2):
                        x2 = x
                        y2 = y + SQUARE_SIZE
                        pygame.draw.line(
                            self.win, BLACK_COLOR, (x, y), (x2, y2), 3)

                    if board[row][col] == BLACK:
                        pygame.draw.circle(
                            self.win, BLACK_COLOR, (x, y), PIECE_RADIUS)
                    elif board[row][col] == WHITE:
                        pygame.draw.circle(
                            self.win, WHITE_COLOR, (x, y), PIECE_RADIUS)

            
