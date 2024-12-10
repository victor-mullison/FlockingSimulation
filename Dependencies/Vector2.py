# Custom Vector2 class for easy math
class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vector2(other.x + self.x, other.y + self.y)
    
    def __sub__(self, other):
        return Vector2(-1 * other.x + self.x, -1 * other.y + self.y)
    
    def __mul__(self, int): # For easy scaling
        return Vector2(self.x * int, self.y * int)
        
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    
    def __truediv__(self, scalar):
        if scalar == 0:
            return self
        return Vector2(self.x / scalar, self.y / scalar)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def limit(self, u_int): # Returns a vector with x and y capped at U_int (for maxspeed)
        if self.x > 0 and self.x > u_int:
            self.x = u_int
        elif self.x < 0 and self.x < u_int * -1:
            self.x = u_int * -1

        if self.y > 0 and self.y > u_int:
            self.y = u_int
        elif self.y < 0 and self.y < u_int * -1:
            self.y = u_int * -1
        
        return self
        
        
    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
        
    def distance_to(self, other):
        diff = other - self
        return diff.length()
    
    def normalize(self): # Works. Trust, brain very big
        self = self / self.length()
        return self
        
    def setMag(self, u_int): #
        self = self.normalize()
        self *= u_int
        return self
    
# Testing vector operations
vec = Vector2(0,10)
vec2 = Vector2(0,5)
