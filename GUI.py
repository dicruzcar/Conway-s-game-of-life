import pygame
import sys, copy
from lifegame import LifeGame
from premade_worlds import PremadeWorlds


class GUI():

    def __init__(self, width=600, height=600, base_unit=5, cps = 30):

        self.height = height
        self.width = width
        self.base_unit = base_unit
        self.white = (0, 0, 0)
        self.black = (255, 255, 255)
        self.cps = cps
        self.pause_CPS = 30
        self.cells = []
        self.pause = True
        self.day = 0
        self.clock = pygame.time.Clock()

        self.window_caption = f"Conway's game of life"

        self.game = LifeGame(
            *self.get_dimension(),
            True
        )
        self.window = pygame.display.set_mode((
            self.width,
            self.height
        ))

        self.premade_worlds = None
        
        self.test_mode = False
        self.main()


    def main(self):
        pygame.init()
        pygame.display.set_caption(self.window_caption)

        while True:
            pygame.display.set_caption(f"{self.window_caption} - day {self.day}")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    #if click cell, then changes the status of the cell
                    self.set_pause(True)
                    position = pygame.mouse.get_pos()
                    for y, row in enumerate(self.cells):
                        for x, cell in enumerate(row):
                            if cell.collidepoint(position):
                                if self.game.world[y][x] == 1:
                                    self.game.world[y][x] = 0
                                    self.game.world_buffer[y][x] = 0
                                    self.game.active_cells.remove((x, y))
                                    self.game.active_cells_copy.remove((x, y))
                                elif self.game.world[y][x] == 0:
                                    self.game.world[y][x] = 1
                                    self.game.world_buffer[y][x] = 1
                                    self.game.active_cells.add((x, y))
                                    self.game.active_cells_copy.add((x, y))
                                self.day = 0
                                
                if event.type == pygame.KEYDOWN:
                    #If SPACE pause
                    if event.key == pygame.K_SPACE:
                        self.set_pause(not self.pause)
                    #if BACKSPACE resets and pause
                    if event.key == pygame.K_BACKSPACE:
                        self.game.clear_world()
                        self.set_pause(True)
                        self.day = 0
                    if event.key == pygame.K_UP:
                        self.scale_cps(2)
                    if event.key == pygame.K_DOWN:
                        self.scale_cps(0.5)
                    if event.key == pygame.K_m:
                        if self.game.world_mode == "normal":
                            self.game.world_mode = "torus"
                            print("Torus world activated")
                        elif self.game.world_mode == "torus":
                            self.game.world_mode = "normal"
                            print("Normal world activated")
                    if event.key == pygame.K_t:
                        self.test_mode = not self.test_mode                    
                    if self.test_mode:
                        if event.key == pygame.K_1:
                            Test = PremadeWorlds()
                            Test.test_1(self.game.world, self.game.active_cells, *self.get_mouse_pos_in_game())
                            self.game.world_buffer = copy.deepcopy(self.game.world)
                            self.game.active_cells_copy = copy.deepcopy(self.game.active_cells)
                        if event.key == pygame.K_2:
                            
                            Test = PremadeWorlds()
                            Test.pulsar(self.game.world, self.game.active_cells, *self.get_mouse_pos_in_game())
                            self.game.world_buffer = copy.deepcopy(self.game.world)
                            self.game.active_cells_copy = copy.deepcopy(self.game.active_cells)

            if not self.pause:
                self.gui_cycle()
                self.day += 1
            else:
                self.paint()


            pygame.display.update()
            self.clock_manager()
        return 0


    def gui_cycle(self):
        self.game.check_world()
        #A world buffer to contrast the world with the buffer and make the changes in the world
        self.game.world_buffer = copy.deepcopy(self.game.world)
        self.game.active_cells_copy = copy.deepcopy(self.game.active_cells)
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

    def get_dimension(self):
        return (int(self.width/self.base_unit), int(self.height/self.base_unit))
    
    def scale_cps(self, scalar):
        value = self.cps*scalar
        if value > 1  and value < 144:
            self.cps = value

    def set_pause(self, pause:bool = True):
        self.pause = pause
        if self.pause:
            self.window_caption = "Conway's game of life (PAUSED)"
            self.clock_manager()
        else:
            self.window_caption = "Conway's game of life"
            self.clock_manager()
    
    def clock_manager(self):
        if self.pause:
            self.clock.tick(self.pause_CPS)
        else:
            self.clock.tick(self.cps)
    
    def get_mouse_pos_in_game(self):
        mouse_pos = pygame.mouse.get_pos()
        return (mouse_pos[0]//self.base_unit, mouse_pos[1]//self.base_unit)

if __name__ == "__main__":
    GUI()