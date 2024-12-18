from Object import *

class Cube(Object):
    def __init__(self, x, y, z):
        Object.__init__(self, x, y, z)
        self.vertices = [(0.5, -0.5, 0.5),#0-
                        (-0.5, -0.5, 0.5),#1-
                        (0.5, 0.5, 0.5),#2-
                        (-0.5, 0.5, 0.5),#3-
                        (0.5, 0.5, -0.5),#4-
                        (-0.5, 0.5, -0.5),#5-
                        (0.5, -0.5, -0.5),#6-
                        (-0.5, -0.5, -0.5),#7-
                        ]
        self.outputBuffer = [arr[:] for arr in self.vertices]

        self.trangles = [0, 2, 3, 0, 3, 1, 2, 4, 5,
                          2, 5, 3, 4, 6, 7, 4, 7, 5,
                          6, 0, 1, 6, 1, 7, 1, 3, 5,
                          1, 5, 7, 6, 4, 2, 6, 2, 0]
        
        
class Pyramid(Object):
    def __init__(self, x, y, z):
        Object.__init__(self, x, y, z)
        self.vertices = [(0.5, -0.5, 0.5),#0-
                        (-0.5, -0.5, 0.5),#1-
                        (0.5, -0.5, -0.5),#2-
                        (-0.5, -0.5, -0.5),#3-
                        (0.0, 0.5, 0.0),#4-
                        ]
                   
        self.outputBuffer = [arr[:] for arr in self.vertices]

        self.trangles = [2, 1, 0, 2, 3, 1,
                         0, 1, 4, 1, 3, 4,
                         3, 2, 4, 2, 0, 4,]
    