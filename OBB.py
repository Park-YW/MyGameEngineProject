import numpy as np
from Object import *

def matrixtoarray(ma : np.matrix):
    return [ma[0, 0], ma[0, 1], ma[0, 2]]

def minusArray(arr):
    return [-arr[0], -arr[1], -arr[2]]

def arrayMulti(A, B):
    return (A[0]*B[0], A[1]*B[1], A[2]*B[2])

class OBB:
    def __init__(self, center, axes, half_sizes):
        self.center = np.array(center)
        self.axes = np.array(axes)  # 3x3 matrix
        self.half_sizes = np.array(half_sizes)  # 3x1 vector

def overlap_on_axis(obb1, obb2, axis):
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

def check_obb_collision(obb1, obb2):
    for i in range(3):
        axis = matrixtoarray(obb1.axes[i])
        if not overlap_on_axis(obb1, obb2, axis):
            return False

        axis = matrixtoarray(-obb2.axes[i])
        if not overlap_on_axis(obb1, obb2, axis):
            return False
        print("ahtj")
        for j in range(3):
            axis = matrixtoarray(np.cross(obb1.axes[i], obb2.axes[j]))
            if np.linalg.norm(axis) > 1e-6:
                if not overlap_on_axis(obb1, obb2, axis):
                    return False

    return True

# 정육면체의 8개 점을 기준으로 OBB 생성
def create_obb_from_cube(cube_vertices):
    center = np.mean(cube_vertices, axis=0)
    axes = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])  # 정육면체의 축
    half_sizes = np.array([1, 1, 1])  # 반 크기 (정육면체의 반 변 길이)

    return OBB(center, axes, half_sizes)

# 정육면체의 8개 점
cube_vertices1 = np.array([
    [1, 1, 1],
    [1, 1, -1],
    [1, -1, 1],
    [1, -1, -1],
    [-1, 1, 1],
    [-1, 1, -1],
    [-1, -1, 1],
    [-1, -1, -1]
])

cube_vertices2 = np.array([
    [0.5, 0.5, 0.5],
    [0.5, 0.5, -0.5],
    [0.5, -0.5, 0.5],
    [0.5, -0.5, -0.5],
    [-0.5, 0.5, 0.5],
    [-0.5, 0.5, -0.5],
    [-0.5, -0.5, 0.5],
    [-0.5, -0.5, -0.5]
])

obb1 = create_obb_from_cube(cube_vertices1)
obb2 = create_obb_from_cube(cube_vertices2)

"""if check_obb_collision(obb1, obb2):
    print("충돌 발생!")
else:
    print("충돌 없음.")"""