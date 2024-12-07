from OpenGL.GL import *
from pyrr import matrix44, quaternion, vector4
#from numpy.matrixlib import *
from numpy import *
from random import *



IDENTITY = matrix([[1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1.0]])


def ToHomo(array = ()):
    if len(array) != 3:
        print("ToHomo Input Error")
        return (0,0,0,1)
    else:
        rearr = list(array)
        rearr.append(1)
        return rearr
    
def ReturnHomo(array = [[]]):
    temp = array.tolist()[0]
    if len(temp) != 4:
        print("ReturnHomo Input Error")
        return (0,0,0)
    else:
        temp.pop()
        return(temp)

def MatrixtoArray(matrix = IDENTITY):
    if matrix.size != 16:
        print("MtoA Input Error")
        return (0,0,0)
    else:
        return (float(matrix[0, 0]), float(matrix[1, 1]), float(matrix[2, 2]))

class Object:
    def __init__(self):
        self.vertices = [(0.5, -0.5, 0.5),
                         (-0.5, -0.5, 0.5),
                         (0.5, 0.5, 0.5),
                         (-0.5, 0.5, 0.5),
                         (0.5, 0.5, -0.5),
                         (-0.5, 0.5, -0.5)]
        self.outputBuffer = [arr[:] for arr in self.vertices]
        self.trangles = [0, 2, 3, 0, 3, 1, ]
        
        self.rotationBuffer = matrix([[1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1.0]])
        self.translationBuffer = matrix([[1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1.0]])
        self.ScaleBuffer = matrix([[1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1.0]])
        self.Color = (1,0,0)
        
    def Rotation(self, axis = 'x', degree = 0):
        Rmatrix = IDENTITY
        
        if axis == 'z': 
            Rmatrix = matrix([  [cos(deg2rad(degree)), sin(deg2rad(degree)), 0, 0],
                                [-sin(deg2rad(degree)), cos(deg2rad(degree)), 0, 0],
                                [0, 0, 1, 0],
                                [0, 0, 0, 1.0]])
        if axis == 'x': 
            Rmatrix = matrix([  [1, 0, 0, 0],
                                [0, cos(deg2rad(degree)), sin(deg2rad(degree)), 0],
                                [0, -sin(deg2rad(degree)), cos(deg2rad(degree)), 0],
                                [0, 0, 0, 1.0]])
        if axis == 'y': 
            Rmatrix = matrix([  [cos(deg2rad(degree)), 0, sin(deg2rad(degree)), 0],
                                [0, 1, 0, 0],
                                [-sin(deg2rad(degree)), 0, cos(deg2rad(degree)), 0],
                                [0, 0, 0, 1.0]])
        
        self.rotationBuffer *= Rmatrix
        
        
    def Translation(self, coord = (0, 0, 0)):
        if len(coord) != 3:
            print("AtoM Input Error")
        else:
            Tmatrix = matrix([  [1, 0, 0, coord[0]],
                                [0, 1, 0, coord[1]],
                                [0, 0, 1, coord[2]],
                                [0, 0, 0, 1.0]])
            self.translationBuffer *= Tmatrix
            
    def Scale(self, size=1.):
        Smatrix = matrix([  [size, 0, 0, 0],
                            [0, size, 0, 0],
                            [0, 0, size, 0],
                            [0, 0, 0, 1.0]])
        self.ScaleBuffer *= Smatrix
        
    def ColorSet(self, color = (1,0,0)):
        self.Color = color

    def draw(self):
        
        for i in range(0, len(self.vertices)):
            self.outputBuffer[i] = ReturnHomo(self.ScaleBuffer@ToHomo(self.vertices[i]))
            self.outputBuffer[i] = ReturnHomo(self.rotationBuffer@ToHomo(self.outputBuffer[i]))
            self.outputBuffer[i] = ReturnHomo(self.translationBuffer@ToHomo(self.outputBuffer[i]))
            
            
        for t in range(0, len(self.trangles), 3):
            glBegin(GL_POLYGON)
            glColor3f(self.Color[0], self.Color[1], self.Color[2])
            glVertex3fv(self.outputBuffer[self.trangles[t]])
            glVertex3fv(self.outputBuffer[self.trangles[t + 1]])
            glVertex3fv(self.outputBuffer[self.trangles[t + 2]])
            glEnd()