import numpy as np
from Object import *

def matrixtoarray(ma : np.matrix):
    return [ma[0, 0], ma[0, 1], ma[0, 2]]

def minusArray(arr):
    return [-arr[0], -arr[1], -arr[2]]

def arrayMulti(A, B):
    return (A[0]*B[0], A[1]*B[1], A[2]*B[2])

def tupleMinus(A, B):
    return (A[0]-B[0], A[1]-B[1], A[2]-B[2],)

def normal(v1, v2, v3):
    vec1 = tupleMinus(v3, v2)
    vec2 = tupleMinus(v1, v2)
    return np.cross(vec1, vec2)


def overlap_on_axis(obb1 : Object, obb2 : Object, axis):
    def project(obb : Object):
        isFirst = True
        centerProjection = np.dot(axis, obb.center)
        for vertex in obb.vertices:
            #projection = matrixtoarray(obb.axes@axis)
            projection = matrixtoarray(obb.axes@arrayMulti(vertex,obb.sizes))
            proj = np.dot(projection,axis)+centerProjection
            
            if isFirst:
                min_proj = proj
                max_proj = proj
                isFirst = False
            else:
                if min_proj > proj:
                    min_proj = proj
                elif max_proj < proj:
                    max_proj = proj
        return min_proj, max_proj

    min1, max1 = project(obb1)
    min2, max2 = project(obb2)

    return not (max1 <= min2 or max2 <= min1)

def check_obb_collision(obb1 : Object, obb2 : Object):
    for i in range(len(obb1.trangles)//3):
        axis = normal(obb1.vertices[obb1.trangles[i*3]], obb1.vertices[obb1.trangles[i*3+1]], obb1.vertices[obb1.trangles[i*3+2]])
        if not overlap_on_axis(obb1, obb2, axis):
            return False
    for i in range(len(obb2.trangles)//3):
        axis = normal(obb2.vertices[obb2.trangles[i*3]], obb2.vertices[obb2.trangles[i*3+1]], obb2.vertices[obb2.trangles[i*3+2]])
        if not overlap_on_axis(obb1, obb2, axis):
            return False

    for i in range(len(obb1.trangles)//3):
        for j in range(len(obb2.trangles)//3):
            for k in range(3):
                vec1 = tupleMinus(obb1.vertices[obb1.trangles[i*3+k]], obb1.vertices[obb1.trangles[i*3+(k+1)%3]])
                vec2 = tupleMinus(obb2.vertices[obb2.trangles[j*3+k]], obb2.vertices[obb2.trangles[j*3+(k+1)%3]])
                axis = np.cross(vec1, vec2)
                if np.linalg.norm(axis) > 1e-6:
                    if not overlap_on_axis(obb1, obb2, axis):
                        return False
 

    return True
