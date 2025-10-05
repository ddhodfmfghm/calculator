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

def main():
    """Основная функция калькулятора"""
    print("Добро пожаловать в калькулятор!")
    print("Доступные операции: +, -, *, /, ^, sqrt")
    
    while True:
        try:
            print("\nВведите операцию (или 'exit' для выхода):")
            operation = input().strip().lower()
            
            if operation == 'exit':
                print("До свидания!")
                break
            elif operation == 'sqrt':
                num = float(input("Введите число: "))
                result = square_root(num)
                print(f"√{num} = {result}")
            else:
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))
                
                if operation == '+':
                    result = add(a, b)
                elif operation == '-':
                    result = subtract(a, b)
                elif operation == '*':
                    result = multiply(a, b)
                elif operation == '/':
                    result = divide(a, b)
                elif operation == '^':
                    result = power(a, b)
                else:
                    print("Неизвестная операция!")
                    continue
                
                print(f"Результат: {a} {operation} {b} = {result}")
                
        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
