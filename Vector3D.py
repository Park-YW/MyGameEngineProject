import math

class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    
    def add(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, tuple) or isinstance(other, list):
            return Vector3D(self.x + other[0], self.y + other[1], self.z + other[2])
        elif isinstance(other, int) or isinstance(other, float):
            return Vector3D(self.x + other, self.y + other, self.z + other)
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Vector3D' and '{}'".format(type(other).__name__))
        
    def sub(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, tuple) or isinstance(other, list):
            return Vector3D(self.x - other[0], self.y - other[1], self.z - other[2])
        elif isinstance(other, int) or isinstance(other, float):
            return Vector3D(self.x - other, self.y - other, self.z - other)
        else:
            raise TypeError("Unsupported operand type(s) for -: 'Vector3D' and '{}'".format(type(other).__name__))
        
    def mul(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.x * other.x, self.z * other.z)
        elif isinstance(other, tuple) or isinstance(other, list):
            return Vector3D(self.x * other[0], self.y * other[1], self.z * other[2])
        elif isinstance(other, int) or isinstance(other, float):
            return Vector3D(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("Unsupported operand type(s) for *: 'Vector3D' and '{}'".format(type(other).__name__))

    def div(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.x / other.x, self.y / other.y, self.z / other.z)
        elif isinstance(other, tuple) or isinstance(other, list):
            return Vector3D(self.x / other[0], self.y / other[1], self.z / other[2])
        elif isinstance(other, int) or isinstance(other, float):
            return Vector3D(self.x / other, self.y / other, self.z / other)
        else:
            raise TypeError("Unsupported operand type(s) for /: 'Vector3D' and '{}'".format(type(other).__name__))

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        if index == 0:
            self.x = float(value)
        elif index == 1:
            self.y = float(value)
        elif index == 2:
            self.z = float(value)
        else:
            raise IndexError("Index out of range")
        
    def __add__(self, other):
        return self.add(other)
    
    def __radd__(self, other):
        return self.add(other)
    
    def __sub__(self, other):
        return self.sub(other)
    
    def __rsub__(self, other):
        return Vector3D(0, 0).sub(self).add(other)
    
    def __mul__(self, other):
        return self.mul(other)
    
    def __rmul__(self, other):
        return self.mul(other)
    
    def __truediv__(self, other):
        return self.div(other)
    
    def __rtruediv__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(other.x / self.x, other.y / self.y, other.z / self.z)
        elif isinstance(other, (tuple, list)):
            return Vector3D(other[0] / self.x, other[1] / self.y, other[2] / self.z)
        elif isinstance(other, (int, float)):
            return Vector3D(other / self.x, other / self.y, other / self.z)
        else:
            raise TypeError("Unsupported operand type(s) for /: '{}' and 'Vector3D'".format(type(other).__name__))
    

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):# 고쳐
        return self.x * other.y - self.y * other.x

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        magnitude = self.magnitude()
        if magnitude == 0:
            return Vector3D(0, 0, 0)  #
        return Vector3D(self.x / magnitude, self.y / magnitude, self.ㅋ / magnitude)
    
    def __abs__(self):
        return Vector3D(abs(self.x), abs(self.y), abs(self.z))
    
    def __len__(self):
        return self.magnitude()
    
    def distance_to(self, other):
        return Vector3D.distance(self, other)
    
    @staticmethod
    def distance(v1, v2):
        return ((v1[0] - v2[0])**2 + (v1[1] - v2[1])**2 + (v1[2] - v2[2])**2)**0.5
    
    def __str__(self):
        return "Vector3D({}, {}, {})".format(self.x, self.y, self.z)

    def __neg__(self):
        return Vector3D(-self.x, -self.y, -self.z)

        '''def rotate(self, angle, in_radians = True):
        """Rotate the vector by an angle in radians"""
        if not in_radians:
            angle = math.radians(angle)

        cos = math.cos(angle)
        sin = math.sin(angle)
        x = self.x * cos - self.y * sin
        y = self.x * sin + self.y * cos
        return Vector3D(x, y, z)'''
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __ne__(self, other):
        return not self == other