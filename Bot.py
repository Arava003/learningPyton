# Алфавит
alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у",
            "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", "1", "2", "3", "4", "5", "6", "7", "8", "9",
            "0", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", ";", "/", "|", ":", "?", "[", "]", "{", "}", "<",
            ">", "~", "`", " ", ".", ",", "+", "-", "_", "=", "Й", "Ц", "У", "К", "Е", "Н", "Г", "Ш", "Щ", "З", "Х",
            "Ъ", "Ф", "Ы", "В", "А", "П", "Р", "О", "Л", "Д", "Ж", "Э", "Я", "Ч", "С", "М", "И", "Т", "Ь", "Б", "Ю",
            "№"]


# Функция просмотра информации по объекту
def data_name(find_name):
    file = open("Numbers_book.txt", "r", encoding="UTF-8")
    book = eval(file.read())
    file.close()
    name_data = f"Информация о человеке '{find_name}'  >>>  "
    number_data = 1
    for i in book[find_name]:
        if number_data == 1:
            name_data += f"Мобильный номер : {i} \n                                      "
            number_data += 1
        elif number_data == 2:
            name_data += f"Домашний номер : {i} \n                                      "
            number_data += 1
        elif number_data == 3:
            name_data += f"Адрес : {i} \n"
    return name_data


# Функция прочтения записей
def read_book(records):
    file = open("Numbers_book.txt", "r", encoding="UTF-8")
    book = eval(file.read())
    file.close()
    records = ""
    number_record = 1
    number_data = 1
    for i in book.keys():
        records += f"Запись номер {number_record}\n"
        records += f"Имя : {i}\nИнформация  >>>  "
        for n in book[i]:
            if number_data == 1:
                records += f"Мобильный номер : {n} \n                 "
                number_data += 1
            elif number_data == 2:
                records += f"Домашний номер : {n} \n                 "
                number_data += 1
            elif number_data == 3:
                records += f"Адрес : {n} \n"
                number_data += 1
            elif number_data > 3:
                records += f"Мобильный номер : {n} \n                 "
                number_data = 2
        number_record += 1
    return records


# Функция добавления информации
def add_number(name, number_1, number_2, address):
    file = open("Numbers_book.txt", "r", encoding="UTF-8")
    book = eval(file.read())
    file.close()
    file = open("Numbers_book.txt", "w", encoding="UTF-8")
    book[name] = [number_1, number_2, address]
    file.write(str(book))
    file.close()
    return "Запись была сохранена"


# Удаление всех записей
def delete_book():
    file_for_delete = open("Numbers_book.txt", "w", encoding="UTF-8")
    file_for_delete.write("{}")
    file_for_delete.close()


# Удаление по определённому имени
def delete_name(name_for_delete):
    file_for_delete = open("Numbers_book.txt", "r", encoding="UTF-8")
    book = eval(file_for_delete.read())
    file_for_delete.close()
    new_book = str(book)
    delete_data = ""
    delete_data = str(book[name_for_delete])
    keys = list(book.keys())
    if keys[len(keys) - 1] == name_for_delete:
        new_book = new_book.replace(delete_data, "")
        new_book = new_book.replace(f", '{name_for_delete}': ", "")
    else:
        new_book = new_book.replace(delete_data, "")
        new_book = new_book.replace(f"'{name_for_delete}': , ", "")
    file_for_delete = open("Numbers_book.txt", "w", encoding="UTF-8")
    file_for_delete.write(str(new_book))
    file_for_delete.close()
    return "Имя удалено"


# Функция шифрования
def shifr(new_text):
    a = ""
    # Проверка на содежание алфавитом символов слова
    for i in text_shifr:
        if i in alphabet:
            a += i
    if a == text_shifr:
        # Шифрование
        step = int(input("Введите длину шага>>>"))
        new_text = ""
        for i in text_shifr:
            for n in alphabet:
                if n == i and alphabet.index(n) + step < 107:
                    new_text += alphabet[alphabet.index(n) + step]
                elif n == i and alphabet.index(n) + step > 106:
                    new_text += alphabet[alphabet.index(n) + step - len(alphabet)]
                else:
                    pass
        # Возврат зашифрованного текста
        return new_text
    # Ошибка, при содержании текста неизвестных символов
    else:
        return "Ошибка! Некоторых символов нет в базе данных! Шифрование не возможно!"


# Функция дешифрования
def deshifr(new_text):
    a = ""
    # Проверка на содержание алфавитом символов слова
    for i in text_deshifr:
        if i in alphabet:
            a += i
    if a == text_deshifr:
        # Дешифрование текста
        step = int(input("Введите длину шага шифрования>>>"))
        new_text = ""
        for i in text_deshifr:
            for n in alphabet:
                if n == i and alphabet.index(n) - step > -1:
                    new_text += alphabet[alphabet.index(n) - step]
                elif n == i and alphabet.index(n) - step < 0:
                    new_text += alphabet[alphabet.index(n) - step + len(alphabet)]
        # Возврат расшифрованного текста
        return new_text
    # Ошибка, при содержании текста неизвестного символа
    else:
        return "Ошибка! Некоторых символов нет в базе данных! Шифрование не возможно!"


# Команды для чат-бота
sl = {"помощь": "Вот мои команды: 'зашифруй'; 'расшифруй';'новая запись';'найти по имени';'вывести записи';'удалить по имени';'удалить все записи'"}
# Приветствующая речь
print("Привет! Если хочешь узнать , что я умею, напиши 'помощь'.")
# Запуск цикла
while True:
    text = input("Введите команду>>> ")
    # Исполнение команд
    if text == "помощь":
        print(sl[text])
        continue
    elif text == "зашифруй":
        text_shifr = input("Вводите текст для шифрования>>> ")
        print(shifr(text_shifr))
        continue
    elif text == "расшифруй":
        text_deshifr = input("Вводите текст для дешифрования>>> ")
        print(deshifr(text_deshifr))
        continue
    elif text == "новая запись":
        name = input("Вводите имя>>> ")
        number_1 = input("Вводите мобильный номер>>> ")
        number_2 = input("Вводите домашний номер>>> ")
        address = input("Вводите адрес>>> ")
        print(add_number(name, number_1, number_2, address))
        continue
    elif text == "найти по имени":
        find_name = input("Вводите имя, по которому вам нужны данные>>> ")
        print(data_name(find_name))
        continue
    elif text == "вывести записи":
        records = ""
        print(read_book(records))
        continue
    elif text == "удалить все записи":
        delete_book()
        print("Записи успешно удалены")
    elif text == "удалить по имени":
        name_for_delete = input("Введите имя, которое хотите удалить>>> ")
        print(delete_name(name_for_delete))
    else:
        print("Ошибка! Такой команды нет!")
        continue
