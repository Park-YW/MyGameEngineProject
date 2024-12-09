from Object import *

class Cube(Object):
    def __init__(self, x, y, z, mass = 1, bounce = 0.5, name = None, is_static = False):
        Object.__init__(self, x, y, z)
        self.vertices = [(0.5, -0.5, 0.5),
                        (-0.5, -0.5, 0.5),
                        (0.5, 0.5, 0.5),
                        (-0.5, 0.5, 0.5),
                        (0.5, 0.5, -0.5),
                        (-0.5, 0.5, -0.5),
                        (0.5, -0.5, -0.5),
                        (-0.5, -0.5, -0.5),
                        (0.5, 0.5, 0.5),
                        (-0.5, 0.5, 0.5),
                        (0.5, 0.5, -0.5),
                        (-0.5, 0.5, -0.5),
                        (0.5, -0.5, -0.5),
                        (0.5, -0.5, 0.5),
                        (-0.5, -0.5, 0.5),
                        (-0.5, -0.5, -0.5),
                        (-0.5, -0.5, 0.5),
                        (-0.5, 0.5, 0.5),
                        (-0.5, 0.5, -0.5),
                        (-0.5, -0.5, -0.5),
                        (0.5, -0.5, -0.5),
                        (0.5, 0.5, -0.5),
                        (0.5, 0.5, 0.5),
                        (0.5, -0.5, 0.5)]
        self.outputBuffer = [arr[:] for arr in self.vertices]

        self.trangles = [0, 2, 3, 0, 3, 1, 8, 4, 5,
                          8, 5, 9, 10, 6, 7, 10, 7, 11,
                          12, 13, 14, 12, 14, 15, 16, 17, 18,
                          16, 18, 19, 20, 21, 22, 20, 22, 23]
        
        
class Ground(Object):
    def __init__(self, x, y, z, mass = 1, bounce = 0.5, name = None, is_static = False):
        Object.__init__(self, x, y, z)
        self.vertices = [(10, -5, 10),
                        (10, -5, -10),
                        (-10, -5, -10),
                        (-10, -5, 10),]
                   
        self.outputBuffer = [arr[:] for arr in self.vertices]

        self.trangles = [0, 2, 3, 0, 3, 1,]
    