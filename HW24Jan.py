from math import*


history_of_answers = []
save_number = int()
print("Здравствуйте. Вы зашли в приложение калькулятор. Вводите примеры в строку, если хотите узнать ответ")
while True:
    question = input("Введите 1, если хотите начать действия с новым числом\nВведите 2, если хотите продолжить работать со старым числом\n >>> ")
    if question == "1":
        examle = (input("Вводите пример >>> ").split())
        print(examle)
        if examle[1] == "+":
            print(int(examle[0]) + int(examle[2]))
            history_of_answers.append(int(examle[0]) + int(examle[2]))
            save_number = int(examle[0]) + int(examle[2])
        elif examle[1] == "-":
            print(int(examle[0]) - int(examle[2]))
            history_of_answers.append(int(examle[0]) - int(examle[2]))
            save_number = int(examle[0]) - int(examle[2])
        elif examle[1] == "/":
            try:
                int(examle[0]) / int(examle[2])
            except ZeroDivisionError:
                print("ERROR\nНевозможно выполнить действие")
            print(int(examle[0]) / int(examle[2]))
            history_of_answers.append(int(examle[0]) / int(examle[2]))
            save_number = int(examle[0]) / int(examle[2])
        elif examle[1] == "//":
            try:
                int(examle[0]) // int(examle[2])
            except ZeroDivisionError:
                print("ERROR\nНевозможно выполнить действие")
            print(int(examle[0]) // int(examle[2]))
            history_of_answers.append(int(examle[0]) // int(examle[2]))
            save_number = int(examle[0]) // int(examle[2])
        elif examle[1] == "*":
            print(int(examle[0]) * int(examle[2]))
            history_of_answers.append(int(examle[0]) * int(examle[2]))
            save_number = int(examle[0]) * int(examle[2])
        elif examle[1] == "**":
            print(int(examle[0]) ** int(examle[2]))
            history_of_answers.append(int(examle[0]) ** int(examle[2]))
            save_number = int(examle[0]) ** int(examle[2])
        elif examle[0] == "sqrt" or examle[0] == "квадрат":
            print(sqrt(int(examle[1])))
            history_of_answers.append(sqrt(int(examle[1])))
            save_number = sqrt(int(examle[1]))
        elif examle[0] == "квадратный" and examle[1] == "корень":
            print(sqrt(int(examle[2])))
            history_of_answers.append(sqrt(int(examle[2])))
            save_number = sqrt(int(examle[2]))
        elif examle[0] == "sin" or examle[0] == "синус":
            print(sin(int(examle[1])))
            history_of_answers.append(sin(int(examle[1])))
            save_number = sin(int(examle[1]))
        elif examle[0] == "cos" or examle[0] == "косинус":
            print(cos(int(examle[1])))
            history_of_answers.append(cos(int(examle[1])))
            save_number = cos(int(examle[1]))
        else:
            print("ERROR\nНевозможно выполнить действие")
    elif question == "2":
        examle = (input("Вводите пример >>> ").split())
        print(examle)
        if examle[0] == "+":
            print(save_number + int(examle[1]))
            history_of_answers.append(save_number + int(examle[1]))
            save_number = save_number + int(examle[1])
        elif examle[0] == "-":
            print(save_number - int(examle[1]))
            history_of_answers.append(save_number - int(examle[1]))
            save_number = save_number - int(examle[1])
        elif examle[0] == "/":
            try:
                save_number / int(examle[1])
            except ZeroDivisionError:
                print("ERROR\nНевозможно выполнить действие")
            print(save_number / int(examle[1]))
            history_of_answers.append(save_number/ int(examle[1]))
            save_number = save_number / int(examle[1])
        elif examle[0] == "//":
            try:
                save_number / int(examle[1])
            except ZeroDivisionError:
                print("ERROR\nНевозможно выполнить действие")
            print(save_number // int(examle[1]))
            history_of_answers.append(save_number // int(examle[1]))
            save_number = save_number // int(examle[1])
        elif examle[0] == "*":
            print(save_number * int(examle[1]))
            history_of_answers.append(save_number * int(examle[1]))
            save_number = save_number * int(examle[1])
        elif examle[0] == "**":
            print(save_number ** int(examle[1]))
            history_of_answers.append(save_number ** int(examle[1]))
            save_number = save_number ** int(examle[1])
        elif examle[0] == "sqrt" or examle[0] == "квадрат":
            print(sqrt(save_number))
            history_of_answers.append(sqrt(save_number))
            save_number = sqrt(save_number)
        elif examle[0] == "квадратный" and examle[1] == "корень":
            print(sqrt(int(examle[2])))
            history_of_answers.append(sqrt(int(examle[2])))
            save_number = sqrt(int(examle[2]))
        elif examle[0] == "sin" or examle[0] == "синус":
            print(sin(int(examle[1])))
            history_of_answers.append(sin(int(examle[1])))
            save_number = sin(int(examle[1]))
        elif examle[0] == "cos" or examle[0] == "косинус":
            print(cos(int(examle[1])))
            history_of_answers.append(cos(int(examle[1])))
            save_number = cos(int(examle[1]))
        else:
            print("ERROR\nНевозможно выполнить действие")
    elif question == "print history" or question == "history" or question == "h" or question == "ph":
        print(history_of_answers)
    else:
        print("ERROR\nНеизвестная команда")
