from OpenGL.GL import *
#from numpy.matrixlib import *
from numpy import *
from random import *



IDENTITY = matrix([[1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1.0]])

def CutRest(hom):
    return matrix([[hom[0,0], hom[0,1], hom[0,2]],
                   [hom[1,0], hom[1,1], hom[1,2]],
                   [hom[2,0], hom[2,1], hom[2,2]]])

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

def MatrixtoArray(matrix : matrix):
    if matrix.size != 16:
        print("MtoA Input Error")
        return (0,0,0)
    else:
        return (float(matrix[0, 0]), float(matrix[1, 1]), float(matrix[2, 2]))

class Object:
    def __init__(self, x, y, z):
        

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
        
        self.center = ReturnHomo((self.translationBuffer@ToHomo((0,0,0))))
        self.axes = CutRest(self.rotationBuffer) # 3x3 matrix
        self.sizes = self.ScaleBuffer  # 3x1 vector

        self.Color = [(0,1,0), (1,0,0), (0,0,1), (1,1,0), (0,1,1), (1,0,1),]

        Tmatrix = matrix([  [1, 0, 0, x],
                            [0, 1, 0, y],
                            [0, 0, 1, z],
                            [0, 0, 0, 1.0]])
        self.translationBuffer *= Tmatrix
    
    def Update(self):
        self.center = ReturnHomo((self.translationBuffer@ToHomo((0,0,0))))
        self.axes = CutRest(self.rotationBuffer)  # 3x3 matrix
        self.sizes = MatrixtoArray(self.ScaleBuffer)  # 3x1 vector

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
            print("Input Error")
        else:
            Tmatrix = matrix([  [1, 0, 0, coord[0]],
                                [0, 1, 0, coord[1]],
                                [0, 0, 1, coord[2]],
                                [0, 0, 0, 1.0]])
            self.translationBuffer *= Tmatrix
            
    def Scale(self, x = 1, y = 1, z = 1):
        Smatrix = matrix([  [x, 0, 0, 0],
                            [0, y, 0, 0],
                            [0, 0, z, 0],
                            [0, 0, 0, 1.0]])
        self.ScaleBuffer *= Smatrix
        
    def ColorSet(self, color = (1,0,0)):
        self.Color = color

    def draw(self, ff):
        
        for i in range(0, len(self.vertices)):
            self.outputBuffer[i] = ReturnHomo(self.ScaleBuffer@ToHomo(self.vertices[i]))
            self.outputBuffer[i] = ReturnHomo(self.rotationBuffer@ToHomo(self.outputBuffer[i]))
            self.outputBuffer[i] = ReturnHomo(self.translationBuffer@ToHomo(self.outputBuffer[i]))
            
        colorcount = 0
        
        for t in range(0, len(self.trangles), 3):
            glBegin(GL_POLYGON)
            tempcolor = self.Color[colorcount//2]
            glColor3f(tempcolor[0], tempcolor[1], tempcolor[2],)
            if ff:
                glColor3f(1,0,0)
            colorcount += 1
            glVertex3fv(self.outputBuffer[self.trangles[t]])
            glVertex3fv(self.outputBuffer[self.trangles[t + 1]])
            glVertex3fv(self.outputBuffer[self.trangles[t + 2]])
            glEnd()