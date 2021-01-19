from math import*


history_of_answers = []
print("Здравствуйте. Вы зашли в приложение калькулятор. Вводите примеры в строку, если хотите узнать ответ")
while True:
    examle = (input("Вводите пример >>> ").split())
    print(examle)
    if examle[1] == "+":
        print(int(examle[0]) + int(examle[2]))
    elif examle[1] == "-":
        print(int(examle[0]) - int(examle[2]))
    elif examle[1] == "/":
        try:
            int(examle[0]) / int(examle[2])
        except ZeroDivisionError:
            print("ERROR\nНевозможно выполнить действие")
        print(int(examle[0]) / int(examle[2]))
    elif examle[1] == "//":
        print(int(examle[0]) // int(examle[2]))
    elif examle[1] == "*":
        print(int(examle[0]) * int(examle[2]))
    elif examle[1] == "**":
        print(int(examle[0]) ** int(examle[2]))
    elif examle[0] == "sqrt" or examle[0] == "квадрат":
        print(sqrt(int(examle[1])))
    elif examle[0] == "квадратный" and examle[1] == "корень":
        print(sqrt(int(examle[2])))
    elif examle[0] == "sin" or examle[0] == "синус":
        print(sin(int(examle[1])))
    elif examle[0] == "cos" or examle[0] == "косинус":
        print(cos(int(examle[1])))
    else:
        print("ERROR\nНевозможно выполнить действие")
