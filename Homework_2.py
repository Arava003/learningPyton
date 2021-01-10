def power(a, n):
    # Возведение числа a в степень n и получение ответа
    return a**n


while True:
    number = power(int(input("Вводите число\n")), int(input("Вводите степень числа\n")))
    print(number)