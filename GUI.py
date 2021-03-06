import pygame
import sys, copy
from lifegame import LifeGame


class GUI():

    def __init__(self, width=600, height=600, base_unit=5, cps = 30):

        self.height = height
        self.width = width
        self.base_unit = base_unit
        self.white = (0, 0, 0)
        self.black = (255, 255, 255)
        self.cps = cps
        self.cells = []
        self.pause = True
        self.day = 0

        self.game = LifeGame(
            int(self.width/self.base_unit),
            int(self.height/self.base_unit),
            True
        )
        self.window = pygame.display.set_mode((
            self.width,
            self.height
        ))

        self.main()


    def main(self):
        pygame.init()
        pygame.display.set_caption(f"Conway's game of life")

        clock = pygame.time.Clock()

        while True:
            pygame.display.set_caption(f"Conway's game of life - day {self.day}")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    #if click cell, then changes the status of the cell
                    position = pygame.mouse.get_pos()
                    for y, row in enumerate(self.cells):
                        for x, cell in enumerate(row):
                            if cell.collidepoint(position):
                                if self.game.world[y][x] == 1:
                                    self.game.world[y][x] = 0
                                    self.game.world_buffer[y][x] = 0
                                elif self.game.world[y][x] == 0:
                                    self.game.world[y][x] = 1
                                    self.game.world_buffer[y][x] = 1
                                self.pause = True
                                self.day = 0
                                
                if event.type == pygame.KEYDOWN:
                    #If SPACE pause
                    if event.key == pygame.K_SPACE:
                        self.pause = not self.pause
                    #if BACKSPACE resets and pause
                    if event.key == pygame.K_BACKSPACE:
                        self.game.clear_world()
                        self.pause = True
                        self.day = 0
            
            if not self.pause:
                self.gui_cycle()
                self.day += 1
            else:
                self.paint()


            pygame.display.update()
            clock.tick(self.cps)
        return 0


    def gui_cycle(self):
        self.game.check_world()
        #A world buffer to contrast the world with the buffer and make the changes in the world
        self.game.world_buffer = copy.deepcopy(self.game.world)
        self.paint()


    def paint(self):
        self.cells = []
        for y, row in enumerate(self.game.world):
            self.cells.append([])
            for x, cell in enumerate(row):
                self.cells[y].append(pygame.Rect(
                                        x*self.base_unit,
                                        y*self.base_unit,
                                        self.base_unit, self.base_unit
                                    ))
                if cell == 0:
                    # print("dead")
                    pygame.draw.rect(self.window, self.white, self.cells[y][x])
                elif cell == 1:
                    # print("alive")
                    pygame.draw.rect(self.window, self.black, self.cells[y][x])


if __name__ == "__main__":
    GUI()