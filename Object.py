from OpenGL.GL import *
from pyrr import matrix44, quaternion, vector4
#from numpy.matrixlib import *
from numpy import *



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
        
        self.rotationBuffer = IDENTITY
        self.transitionBuffer = IDENTITY
        
    def Rotation(self, axis, degree):
        Rmatrix = IDENTITY
        
        if axis == 'x':
            Rmatrix = matrix([  [cos(deg2rad(degree)), sin(deg2rad(degree)), 0, 0],
                                [-sin(deg2rad(degree)), cos(deg2rad(degree)), 0, 0],
                                [0, 0, 1, 0],
                                [0, 0, 0, 1.0]])
        
        self.rotationBuffer *= Rmatrix
        
        
    def Trasition(self, coord = (0, 0, 0)):
        if len(coord) != 3:
            print("AtoM Input Error")
        else:
            Tmatrix = matrix([  [1, 0, 0, coord[0]],
                                [0, 1, 0, coord[1]],
                                [0, 0, 1, coord[2]],
                                [0, 0, 0, 1.0]])
            self.transitionBuffer *= Tmatrix

    def draw(self):
        
        for i in range(0, len(self.vertices)):
            
            self.outputBuffer[i] = ReturnHomo(self.rotationBuffer@ToHomo(self.vertices[i]))
            self.outputBuffer[i] = ReturnHomo(self.rotationBuffer@ToHomo(self.outputBuffer[i]))
            
        for t in range(0, len(self.trangles), 3):
            glBegin(GL_POLYGON)
            glVertex3fv(self.outputBuffer[self.trangles[t]])
            glVertex3fv(self.outputBuffer[self.trangles[t + 1]])
            glVertex3fv(self.outputBuffer[self.trangles[t + 2]])
            glEnd()