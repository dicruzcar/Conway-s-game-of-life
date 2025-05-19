import random
import time
import copy

#Available axis values: "x" and "y"

class LifeGame():

    def __init__(self, width, height, gui = False, world_mode = "normal"):
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
        self.active_cells = set()
        self.active_cells_copy = set()

        for i in range(self.cells):
            pos = self.get_random_position(self.width, self.height)
            self.generate_cells(pos)

        self.alive_symbol = "X"
        self.dead_symbol = " "

        if not self.gui:
            self.game_cycle()
        self.world_mode = world_mode
        self.get_neighborhood = self.get_neighborhood_normal
        

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
            self.active_cells.add(pos)
        elif (self.world_buffer[pos[1]][pos[0]] == 1) and ((counter != 2) and (counter != 3)):
            self.world[pos[1]][pos[0]] = 0
            self.active_cells.remove(pos)
    

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
    
    def get_neighborhood_normal(self, x, y):
        x_bound = self.__get_edge_by_axis("x")
        y_bound = self.__get_edge_by_axis("y")

        if(x == 0): 
            if (y == 0): return [
                                (x+1, y),
                    (x, y+1),   (x+1, y+1),     

            ]

            if (y == y_bound): return [

                    (x, y-1),   (x+1, y-1),
                                (x+1, y),
                ]
            
            return [
                (x, y-1),   (x+1, y-1),
                            (x+1, y),
                (x, y+1),   (x+1, y+1),
            ]


        if(x == x_bound):
            if (y == 0): return [
                (x-1,y),
                (x-1,y+1),  (x, y+1),

            ]

            if (y == y_bound): return [

                (x-1,y-1),  (x, y-1),
                (x-1,y),
            ]
            
            return [
                (x-1,y-1),  (x, y-1),
                (x-1,y),
                (x-1,y+1),  (x, y+1),
            ]

        if (y == 0): return [
            (x-1,y),                (x+1, y),
            (x-1,y+1),  (x, y+1),   (x+1, y+1),

        ]

        if (y == y_bound): return [

            (x-1,y-1),  (x, y-1),   (x+1, y-1),
            (x-1,y),                (x+1, y),
        ]
        
        return [
            (x-1,y-1),  (x, y-1),   (x+1, y-1),
            (x-1,y),                (x+1, y),
            (x-1,y+1),   (x, y+1),   (x+1, y+1),
        ]





    def get_neighborhood_torus(self, x, y):
        #This functions objective is to calculate the neighborhood of a cell
        #In this specific case, it returns the neighborhood of a cell in a toroidal world
        #This means that if the cell is at the edge of the world, it will wrap around to the other side, creating a continuous space
        x_bound = self.__get_edge_by_axis("x")
        y_bound = self.__get_edge_by_axis("y")

        if(x == 0): 
            if (y == 0): return [
                    (x_bound, y_bound),(x, y_bound),(x+1, y_bound),
                    (x_bound, y),                   (x+1, y),
                    (x_bound, y+1),       (x, y+1),   (x+1, y+1)     
                ]
            
            if (y == y_bound > 0): return [
                    (x_bound, y-1),      (x, y-1),    (x+1, y-1),
                    (x_bound, y),                     (x+1, y),
                    (x_bound, 0),       (x, 0),   (x+1, 0)  
                ]
    
            
            return [
                (x_bound, y-1),      (x, y-1),    (x+1, y-1),
                (x_bound, y),                     (x+1, y),
                (x_bound, y+1),       (x, y+1),   (x+1, y+1)  
            ]


        if(x == x_bound):
            if (y == 0): return [
                    (x-1, y_bound),(x, y_bound),(0, y_bound),
                    (x-1,y),                (0, y),
                    (x-1, y+1),     (x, y+1),   (0, y+1)
                ]
             
            if (y == y_bound): return [
                    (x-1, y-1),(x, y-1),(0, y-1),
                    (x-1,y),                   (0, y),
                    (x-1,0),(x,0),   (0,0) 
            ]

            #If y != 0 and y != y_bound then y is in the middle
            return [
                (x-1, y-1),(x, y-1),(0, y-1),
                (x-1,y),                (0, y),
                (x-1, y+1),     (x, y+1),   (0, y+1) 
            ]

        #Same here, if x is not 0 and x is not the x_bound then x is in the middle, so we dont need to addd an inneccesary condition
        #if both conditions meet, then of course that x is in middle of between the edges 0 < x < x_bound 

        if (y == 0): return [
                (x-1, y_bound),(x, y_bound),(x+1, y_bound),
                (x-1,y),                (x+1, y),
                (x-1,y+1),  (x, y+1),   (x+1, y+1),
            ]
        
        if (y == y_bound): return [
                (x-1,y-1),  (x, y-1),   (x+1, y-1),
                (x-1,y),                (x+1, y),
                (x-1, 0),     (x, 0),   (x+1, 0)  
            ]
        
        return [
                (x-1,y-1),  (x, y-1),   (x+1, y-1),
                (x-1,y),                (x+1, y),
                (x-1,y+1),   (x, y+1),   (x+1, y+1),
        ]
    
    def check_world(self):
        self.set_neighborhood_calculation()
        for x,y in self.active_cells_copy:
            neighborhood = self.get_neighborhood(x,y)
            self.check_state(
                (x,y), 
                neighborhood
            )
            for neighbor in neighborhood:
                if neighbor not in self.active_cells_copy:
                    self.check_state(
                        neighbor, 
                        self.get_neighborhood(neighbor[0], neighbor[1])
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
        self.active_cells_copy = copy.deepcopy(self.active_cells)

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
        self.active_cells = set()
        self.active_cells_copy = set()

    def set_neighborhood_calculation(self):
        if self.world_mode == "normal":
            self.get_neighborhood = self.get_neighborhood_normal
        elif self.world_mode == "torus":
            self.get_neighborhood = self.get_neighborhood_torus
