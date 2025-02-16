class IncorrectTriangleSides(Exception):
    """Исключение, которое выбрасывается при некорректных сторонах треугольника"""
    pass

def get_triangle_type(a, b, c):
    """
    Функция определяет тип треугольника по длинам его сторон.

    :param a: длина первой стороны
    :param b: длина второй стороны
    :param c: длина третьей стороны
    :return: строка типа треугольника: "nonequilateral", "isosceles", "equilateral"

    Примеры:
    >>> get_triangle_type(3, 3, 3)
    'equilateral'
    >>> get_triangle_type(3, 4, 3)
    'isosceles'
    >>> get_triangle_type(3, 4, 5)
    'nonequilateral'
    >>> get_triangle_type(1, 1, 2)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides: Некорректные стороны треугольника
    >>> get_triangle_type(0, 1, 1)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides: Некорректные стороны треугольника
    >>> get_triangle_type(5, 5, 5)
    'equilateral'
    >>> get_triangle_type(7, 10, 7)
    'isosceles'
    """
    
    # Проверка корректности сторон
    if a <= 0 or b <= 0 or c <= 0:
        raise IncorrectTriangleSides("Некорректные стороны треугольника")
    
    # Проверка на существование треугольника
    if a + b <= c or a + c <= b or b + c <= a:
        raise IncorrectTriangleSides("Некорректные стороны треугольника")
    
    # Определение типа треугольника
    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "nonequilateral"


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)  # Запуск тестов с подробным выводом
