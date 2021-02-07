import sqlite3


while True:
    connect = sqlite3.connect("himeworking.db")
    cursor = connect.cursor()

    humans = "humans"

    print("Здравствуйте. Вы зашли на сайт форума любителей кактусов.")
    answer = input("Вы хотите войти или зарегистрироваться?")
    if answer in ("Зарегистрироваться", "registration"):
        name = input("Вводите имя >>> ")
        password = input("Вводите придуманный пароль >>> ")
        info = input("Вводите информацию о себе >>> ")
        cursor.execute(f'select * from humans where name="{name}"')
        if cursor.fetchall():
            print("Пользоватль с таким именем уже есть. Пожалуйтса выберете другое имя.")
            continue
        cursor.execute(f'insert into humans values ("{name}", "{password}", "{info}")')
        print("Регистрация прошла успешно")
    elif answer in ("Войти", "login", "sign in"):
        user_name = input("Вводите своё имя >>> ")
        user_password = input("Вводите свой пароль")
        cursor.execute(f'select * from "{humans}" where name="{user_name}" and password="{user_password}"')
        data = cursor.fetchall()
        if data:
            print(f"Здравствуйте {data[0][0]}! \nДобро пожаловать на сайт. \nВот информация, которую вы вводили")
            print(f"Имя -- {data[0][0]}\nИнформация о себе -- {data[0][2]}")
        else:
            print("Некорректные данные")
    elif answer in ("redact", "redact info", "редактировать"):
        user_name = input("Вводите своё имя >>> ")
        user_password = input("Вводите свой пароль")
        cursor.execute(f'select * from "{humans}" where name="{user_name}" and password="{user_password}"')
        data = cursor.fetchall()
        if data:
            redact = input("Что вы хотите редактировать")
            if redact in ("name", "имя"):
                new_name = input("Вводите новое имя >>>")
                cursor.execute(f'update humans set name="{new_name}" where name="{user_name}"')
            elif redact in ("password", "пароль"):
                new_password = input("Вводите новый пароль >>>")
                cursor.execute(f'update humans set password="{new_password}" where password="{user_password}"')
            elif redact in ("info", "информация"):
                new_info = input("Вводите новое описание >>> ")
                cursor.execute(f'update humans set info="{new_info}" where info="{data[0][2]}"')
            else:
                print("Некорректная команда")
    elif answer == "data":
        cursor.execute(f'select * from humans')
        print(cursor.fetchall())

    connect.commit()