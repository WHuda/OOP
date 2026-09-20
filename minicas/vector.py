import math


class Vector2D:
    """Вектор на плоскости"""
    
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
        
    def length(self) -> float:
        return math.hypot(self.x, self.y)
    
    def scaled(self, k: float) -> "Vector2D":
        return Vector2D(self.x * k, self.y * k)
        
    def __repr__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"