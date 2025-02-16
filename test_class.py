import pytest
from triangle_class import Triangle, IncorrectTriangleSides

# Позитивные тесты
def test_valid_triangle():
    t = Triangle(3, 4, 5)
    assert t.triangle_type() == "nonequilateral"
    assert t.perimeter() == 12

def test_equilateral_triangle():
    t = Triangle(5, 5, 5)
    assert t.triangle_type() == "equilateral"
    assert t.perimeter() == 15

def test_isosceles_triangle():
    t = Triangle(5, 5, 8)
    assert t.triangle_type() == "isosceles"
    assert t.perimeter() == 18

# Негативные тесты
def test_invalid_triangle_sides_zero():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 4, 5)

def test_invalid_triangle_sides_negative():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-3, 4, 5)

def test_invalid_triangle_sides_not_a_triangle():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 1, 3)

def test_invalid_triangle_sides_negative_and_zero():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, -3, 5)
