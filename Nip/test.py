import pygame
import math

WIDTH, HEIGHT = 800, 800
BOARD_COLOR = (0, 180, 0)
GRID_COLOR = (0, 0, 0)
ROWS, COLS = 8, 8
RADIUS = min(WIDTH, HEIGHT) // 2 - 10
DISC_RADIUS = RADIUS // 10

board = [
    [0] * COLS for _ in range(ROWS)
]

class Map:
    def __init__(self, win):
        self.win = win

    def draw(self):
        self.win.fill(BOARD_COLOR)

        center_x, center_y = WIDTH // 2, HEIGHT // 2

        # Draw the main circular field
        pygame.draw.circle(self.win, GRID_COLOR, (center_x, center_y), RADIUS, 2)

        # Draw the gridlines
        for angle in range(0, 360, 45):
            x1 = center_x + int(RADIUS * math.cos(math.radians(angle)))
            y1 = center_y + int(RADIUS * math.sin(math.radians(angle)))
            x2 = center_x + int(RADIUS * math.cos(math.radians(angle + 180)))
            y2 = center_y + int(RADIUS * math.sin(math.radians(angle + 180)))
            pygame.draw.line(self.win, GRID_COLOR, (x1, y1), (x2, y2), 2)

        # Draw pieces
        for row in range(ROWS):
            for col in range(COLS):
                angle = math.radians((row * COLS + col) * (360 / (ROWS * COLS)))
                x = center_x + int(RADIUS * math.cos(angle))
                y = center_y + int(RADIUS * math.sin(angle))

                if board[row][col] == 1:
                    pygame.draw.circle(self.win, GRID_COLOR, (x, y), DISC_RADIUS)
                elif board[row][col] == -1:
                    pygame.draw.circle(self.win, GRID_COLOR, (x, y), DISC_RADIUS)

# Pygame setup
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nip (Reversi)")

# Main game loop
running = True
map_game = Map(win)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    map_game.draw()
    pygame.display.flip()

pygame.quit()
