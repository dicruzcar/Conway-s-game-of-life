import pygame
import sys
from lifegame import LifeGame


class GUI():

    def __init__(self, width=600, height=600, base_unit=5, cps = 5):

        self.height = height
        self.width = width
        self.base_unit = base_unit
        self.white = (0, 0, 0)
        self.black = (255, 255, 255)
        self.cps = cps
        self.cells = []
        self.pause = True

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
        pygame.display.set_caption("Juego de la vida")

        clock = pygame.time.Clock()

        while True:            
            for eventos in pygame.event.get():
                if eventos.type == pygame.QUIT:
                    sys.exit(0)
                if eventos.type == pygame.MOUSEBUTTONDOWN and eventos.button == 1:
                    position = pygame.mouse.get_pos()
                    for y, row in enumerate(self.cells):
                        for x, cell in enumerate(row):
                            if cell.collidepoint(position):
                                print("OLD", self.game.world_buffer[y][x]==1)
                                if self.game.world[y][x] == 1:
                                    self.game.world[y][x] = 0
                                    self.game.world_buffer[y][x] = 0
                                elif self.game.world[y][x] == 0:
                                    self.game.world[y][x] = 1
                                    self.game.world_buffer[y][x] = 1
                                """ print("OLD", self.game.world_buffer[y][x])
                                self.game.world[y][x] = 1 if self.game.world[y][x] == 1 else 0
                                self.game.world_buffer[y][x] = 1 if self.game.world_buffer[y][x] == 1 else 0
                                print("NEW", self.game.world_buffer[y][x]) """
                                print("NEW", self.game.world_buffer[y][x])
                                self.pause = True
                if eventos.type == pygame.KEYDOWN:
                    self.pause = True
            
            # print("hi")
            if not self.pause:
                self.gui_cycle()
            else:
                self.paint()


            pygame.display.update()
            clock.tick(self.cps)
        return 0


    def gui_cycle(self):
        self.paint()
        # game.print_world()
        self.game.check_world()
        self.game.world_buffer = self.game.world.copy()


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