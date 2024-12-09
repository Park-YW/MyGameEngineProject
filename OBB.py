import numpy as np

def matrixtoarray(ma : np.matrix):
    return [ma[0, 0], ma[0, 1], ma[0, 2]]

def minusArray(arr):
    return [-arr[0], -arr[1], -arr[2]]

class OBB:
    def __init__(self, center, axes, half_sizes):
        self.center = np.array(center)
        self.axes = np.array(axes)  # 3x3 matrix
        self.half_sizes = np.array(half_sizes)  # 3x1 vector

def overlap_on_axis(obb1, obb2, axis):
    def project(obb):
        projection = matrixtoarray(obb.axes@axis)
        centerProjection = np.dot(axis, obb.center)
        proj1 = np.dot(projection,minusArray(obb.half_sizes))+centerProjection
        proj2 = np.dot(projection,obb.half_sizes)+centerProjection
        if proj1 > proj2:
            min_proj = proj2
            max_proj = proj1
        else:
            min_proj = proj1
            max_proj = proj2
        return min_proj, max_proj

    min1, max1 = project(obb1)
    min2, max2 = project(obb2)

    print(min1, max1, min2, max2)
    print(not (max1 < min2 or max2 < min1))

    return not (max1 <= min2 or max2 <= min1)

def check_obb_collision(obb1, obb2):
    rr = True
    r2 = True
    print("nor")
    for i in range(3):
        axis = matrixtoarray(obb1.axes[i])
        if not overlap_on_axis(obb1, obb2, axis):
            rr = False

        axis = matrixtoarray(-obb2.axes[i])
        if not overlap_on_axis(obb1, obb2, axis):
            rr = False
    
    print("ex")
    for i in range(3):
        for j in range(3):
            axis = matrixtoarray(np.cross(obb1.axes[i], obb2.axes[j]))
            if np.linalg.norm(axis) > 1e-6:
                if not overlap_on_axis(obb1, obb2, axis) and not j == 1:
                    r2 = False

    return rr or r2

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