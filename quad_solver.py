import math

def solve_quad(a, b, c):
    
    if a == 0:
        if b == 0:
            return [] if c != 0 else ["Бесконечное множество"]
        return [-c / b]
    
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return []
    elif discriminant == 0:
        return [-b / (2 * a)]
    else:
        root1 = (-b - math.sqrt(discriminant)) / (2 * a)
        root2 = (-b + math.sqrt(discriminant)) / (2 * a)
        return sorted([root1, root2])
