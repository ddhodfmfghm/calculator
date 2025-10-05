def add(a, b):
    """Сложение двух чисел"""
    return a + b

def subtract(a, b):
    """Вычитание двух чисел"""
    return a - b

def multiply(a, b):
    """Умножение двух чисел"""
    return a * b

def divide(a, b):
    """Деление двух чисел"""
    if b == 0:
        raise ValueError("Ошибка: Деление на ноль!")
    return a / b

def power(a, b):
    """Возведение a в степень b"""
    return a ** b

def square_root(a):
    """Вычисление квадратного корня"""
    if a < 0:
        raise ValueError("Ошибка: Нельзя извлечь корень из отрицательного числа!")
    return a ** 0.5
