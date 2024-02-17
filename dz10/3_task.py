def fibonacci(n):
    """
    Returns fibonacci.
    """
    if n <= 0:
        return "Введите положительное целое число для последовательности Фибоначчи"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = fibonacci(n - 1)
        fib.append(fib[-1] + fib[-2])
        return fib

if __name__ == "__main__":
    n = int(input("Введите число: "))
    a = 0
    result = fibonacci(n)
    for i in result:
        a += i - (i - 1)
        print(f"fibonacci {a} = {i} ")
