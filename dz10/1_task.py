"""
1 task
"""
import math

def factorial(n):
    """
    Returns factorial.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    """
    Returns fibonacci.
    """
    if n <= 0:
        return "Введите положительное целое число для последовательности Фибоначчи"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("Добро пожаловать в инженерный калькулятор!")

while True:


    choice = input("Выберите операцию: 1. Арифметические операции, 2. Нахождение факториала, 3. Последовательность Фибоначчи, 4. Тригонометрические функции, 5. Возведение в степень, 6. Выход")

    if choice == '1':
        ari1 = input("Введите 1 число: ")
        ari2 = input("Введите 2 число: ")
        add = ari1 + ari2
        sub = ari1 - ari2
        mul = ari1 * ari2
        div = ari1 / ari2
        print(f"Результат: сумма({add}), разность({sub}), произведение({mul}), частное({div})")
    elif choice == '2':
        num = int(input("Введите число для нахождения факториала: "))
        result = factorial(num)
        print("Факториал:", result)
    elif choice == '3':
        num = int(input("Введите номер элемента в последовательности Фибоначчи: "))
        result = fibonacci(num)
        print("Элемент Фибоначчи:", result)
    elif choice == '4':
        angle = float(input("Введите угол в радианах: "))
        print("sin:", math.sin(angle))
        print("cos:", math.cos(angle))
        print("tan:", math.tan(angle))
    elif choice == '5':
        base = float(input("Введите основание: "))
        exponent = float(input("Введите показатель степени: "))
        result = math.pow(base, exponent)
        print("Результат возведения в степень:", result)
    elif choice == '6':
        break
    else:
        print("Некорректный ввод. Пожалуйста, выберите существующую операцию.")
