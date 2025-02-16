class IncorrectTriangleSides(Exception):
    pass

class Triangle:
    def __init__(self, a, b, c):
   
        if a <= 0 or b <= 0 or c <= 0:
            raise IncorrectTriangleSides("Некорректные стороны треугольника")
        
        if a + b <= c or a + c <= b or b + c <= a:
            raise IncorrectTriangleSides("Некорректные стороны треугольника")
        
        self.a = a
        self.b = b
        self.c = c

    def triangle_type(self):
   
        if self.a == self.b == self.c:
            return "equilateral"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "isosceles"
        else:
            return "nonequilateral"

    def perimeter(self):
  
        return self.a + self.b + self.c
