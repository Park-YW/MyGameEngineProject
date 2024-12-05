from Object import *

def ArraytoMatrix(array = ()):
    if len(array) != 3:
        print("AtoM Input Error")
        return IDENTITY
    else:
        return matrix([[array[0], 0, 0, 0],
                [0, array[1], 0, 0],
                [0, 0, array[2], 0],
                [0, 0, 0, 1.0]])


aaaa = (0.5, -0.5, 0.5, 1)
ff = ()
coord = (0,0,10)
ddd = IDENTITY
#print(ddd.tolist())
#print(ddd)

Tmatrix = matrix([  [1, 0, 0, coord[0]],
                                [0, 1, 0, coord[1]],
                                [0, 0, 1, coord[2]],
                                [0, 0, 0, 1.0]])

print(ReturnHomo(Tmatrix@ToHomo(coord)))
print(coord)

