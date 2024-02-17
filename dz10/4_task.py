def is_power_of_two(number):
    if number <= 0:
        return False
    
    while number % 2 == 0:
        number //= 2
    
    return number == 1

if __name__ == "__main__":
    num = int(input("Введите число: "))
    result = is_power_of_two(num)
    print(result)