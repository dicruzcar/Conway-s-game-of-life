
#Careful, this functions mutate the world, they do not return a new world, so be careful with the world argument you pass to them.
class PremadeWorlds():
    def __init__(self):
        pass
    def test_1(self, world, active_cells, px, py):
    
        world[py+1][px-1] = 1
        world[py][px-1] = 1
        world[py-1][px-1] = 1
        world[py][px] = 1

        active_cells.add((px-1, py+1))
        active_cells.add((px-1, py))
        active_cells.add((px-1, py-1))
        active_cells.add((px, py))
    
    def pulsar(self, world, active_cells, px, py): 
        self.__base_pulsar(world, active_cells, px, py, 1, 1)
        self.__base_pulsar(world, active_cells, px, py, -1, 1)
        self.__base_pulsar(world, active_cells, px, py, 1, -1)
        self.__base_pulsar(world, active_cells, px, py, -1, -1)

    
    def __base_pulsar(self, world, active_cells, px, py, x_mirroring = 1, y_mirroring = 1):
        #Reflection can be used for scaling but lets keep it simple for now
        offset = 5
        self.__base_3_point_line(world, 
                                active_cells, 
                                px-(2*x_mirroring),
                                py-(1*y_mirroring), 
                                "h",
                                x_mirroring
        )
        self.__base_3_point_line(world, 
                                active_cells, 
                                px-(1*x_mirroring),
                                py-(2*y_mirroring),
                                "v",
                                y_mirroring
        )
        self.__base_3_point_line(world, 
                                active_cells, 
                                px-(2*x_mirroring), 
                                py-((1+offset)*y_mirroring), 
                                "h",
                                x_mirroring
        )
        self.__base_3_point_line(world, 
                                active_cells, 
                                px-((1+offset)*x_mirroring), 
                                py-(2*y_mirroring), 
                                "v",
                                y_mirroring
        )        


    def __base_3_point_line(self, world, active_cells, px, py, orientation, mirroring = 1):
        mirroring = -mirroring
        if orientation == "v":
            world[py][px] = 1
            world[py+(1*mirroring)][px] = 1
            world[py+(2*mirroring)][px] = 1
            active_cells.add((px, py))
            active_cells.add((px, py+(1*mirroring)))
            active_cells.add((px, py+(2*mirroring)))
        elif orientation == "h":
            world[py][px] = 1
            world[py][px+(1*mirroring)] = 1
            world[py][px+(2*mirroring)] = 1
            active_cells.add((px, py))
            active_cells.add((px+(1*mirroring), py))
            active_cells.add((px+(2*mirroring), py))
        return (world, active_cells)