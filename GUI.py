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
            # print("hi")
            self.gui_cycle()

            for eventos in pygame.event.get():
                if eventos.type == pygame.QUIT:
                    sys.exit(0)

            pygame.display.update()
            clock.tick(self.cps)
        return 0


    def gui_cycle(self):
        self.paint()
        # game.print_world()
        self.game.check_world()
        self.game.world_buffer = self.game.world.copy()


    def paint(self):
        for y, row in enumerate(self.game.world):
            for x, cell in enumerate(row):
                if cell == 0:
                    # print("dead")
                    pygame.draw.rect(self.window, self.white,
                                    pygame.Rect(
                                        x*self.base_unit,
                                        y*self.base_unit,
                                        self.base_unit, self.base_unit
                                    )
                                    )
                elif cell == 1:
                    # print("alive")
                    pygame.draw.rect(self.window, self.black,
                                    pygame.Rect(
                                        x*self.base_unit,
                                        y*self.base_unit,
                                        self.base_unit, self.base_unit
                                    )
                                    )


if __name__ == "__main__":
    GUI()