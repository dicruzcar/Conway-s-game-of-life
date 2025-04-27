import random
import time
import copy

#Available axis values: "x" and "y"

class LifeGame():

    def __init__(self, width, height, gui = False):
        self.world = [ 
                        [ 0 for inx in range(width)]
                        for iny in range(height)
                    ] 
        self.width = width
        self.height = height
        if gui:
            self.cells = 0
        else:
            self.cells = random.randint(int((width*height)/20), int((width*height)/20))
        self.gui = gui
        self.world_buffer = copy.deepcopy(self.world)

        for i in range(self.cells):
            pos = self.get_random_position(self.width, self.height)
            self.generate_cells(pos)

        self.alive_symbol = "X"
        self.dead_symbol = " "

        if not self.gui:
            self.game_cycle()
        

    def get_random_position(self, width, height):
        return(
            random.randint(0, width-1),
            random.randint(0, height-1)
            )

    def generate_cells(self, pos):
            if self.world[pos[1]][pos[0]] != 1:
                self.world[pos[1]][pos[0]] = 1
                return 0
            else:
                pos = self.get_random_position(self.width, self.height)
                self.generate_cells(pos)

    def check_state(self, pos, family):
        counter = 0
        for values in family:
            if self.world_buffer[values[1]][values[0]] == 1:
                counter += 1

        if (self.world_buffer[pos[1]][pos[0]] == 0) and counter == 3:
            self.world[pos[1]][pos[0]] = 1
        elif (self.world_buffer[pos[1]][pos[0]] == 1) and ((counter != 2) and (counter != 3)):
            self.world[pos[1]][pos[0]] = 0

    def __which_edge(self, index, axis):
        end_edge = self.__get_edge_by_axis(axis)
        return index if (index == 0 or index == end_edge) else -1
    
    def __get_edge_by_axis(self, axis):
        #Be Careful, this returns the edge based on count starting at zero, so you never get index out of bounds
        #Valid axis: "x" and "y", otherwise will raise an error
        if(axis != "x" and axis != "y"):
            raise ValueError("Axis value not defined")
        response = self.width - 1
        if (axis == "y"): response = self.height - 1
        return response
    
    def get_neighborhood(self, x, y):
        neighborhood = []
        x_edge = self.__which_edge(x, "x")
        y_edge = self.__which_edge(y, "y")

        if(x_edge == 0): 
            if (y_edge == 0):
                neighborhood = [
                                (x+1, y),
                    (x, y+1),   (x+1, y+1),     

                ]
            
            if (y_edge < 0):
                neighborhood = [
                    (x, y-1),   (x+1, y-1),
                                (x+1, y),
                    (x, y+1),   (x+1, y+1),
                ]

            if (y_edge > 0):
                neighborhood = [

                    (x, y-1),   (x+1, y-1),
                                (x+1, y),
                ]

        if(x_edge < 0):
            if (y_edge == 0):
                neighborhood = [
                    (x-1,y),                (x+1, y),
                    (x-1,y+1),  (x, y+1),   (x+1, y+1),

                ]

            if (y_edge < 0):
                neighborhood = [
                    (x-1,y-1),  (x, y-1),   (x+1, y-1),
                    (x-1,y),                (x+1, y),
                    (x-1,y+1),   (x, y+1),   (x+1, y+1),
            ]

            if (y_edge > 0):
                neighborhood = [

                    (x-1,y-1),  (x, y-1),   (x+1, y-1),
                    (x-1,y),                (x+1, y),
                ]

        if(x_edge > 0):
            if (y_edge == 0):
                neighborhood = [
                                (x-1,y),
                                (x-1,y+1),  (x, y+1),

                ]

            if (y_edge < 0):
                neighborhood = [
                                (x-1,y-1),  (x, y-1),
                                (x-1,y),
                                (x-1,y+1),  (x, y+1),
                ]

            if (y_edge > 0):
                neighborhood = [

                                (x-1,y-1),  (x, y-1),
                                (x-1,y),
                ]

        return neighborhood

    
    def check_world(self):
        for y,row in enumerate(self.world_buffer):
            for x,_ in enumerate(row):
                self.check_state(
                    (x,y), 
                    self.get_neighborhood(x,y)
                )

    def print_world(self):
        for row in self.world:
            buffer = ""
            for cell in row:
                if cell == 1:
                     buffer += self.alive_symbol
                elif cell == 0:
                    buffer += self.dead_symbol
            print(buffer)
        print(" ")

    def step(self):
        self.print_world()
        self.check_world()
        self.world_buffer = copy.deepcopy(self.world)

    def game_cycle(self):
        while(True):
            self.step()
            time.sleep(1)

    def clear_world(self):
        self.world = [ 
                        [ 0 for inx in range(self.width)]
                        for iny in range(self.height)
                    ]
        self.world_buffer = copy.deepcopy(self.world)
