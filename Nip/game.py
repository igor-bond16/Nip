import pygame
import sys
import math
from settings import *
from map import Map
from ai import AI
from player import Player

class Game:
    def __init__(self):
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.map = Map(self.win)
        self.ai = AI(self.win)
        self.player = Player(self.win)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    # print(y//SQUARE_SIZE,x//SQUARE_SIZE)
                    self.ai.determine_direction(y//SQUARE_SIZE,x//SQUARE_SIZE)

            self.map.draw()


            pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.run()
