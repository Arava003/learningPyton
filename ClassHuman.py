import random


class Human():
    # Создание человека и ввод его параметров
    def __init__(self, name="Михаил", age=14, height=175, weight=73):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.status = "Бодрствует"
        self.health = 100
        self.satiety = 100
        self.emotion = "Радость"
        self.stress = 0

    # Вывод всех характеристик человека
    def data(self):
        self.arr = [
            f"Имя -  {self.name}; Возраст - {self.age}; Рост - {self.height}; Вес - {self.weight}; Статус - {self.status}; Показатель здоровья - {self.health}; Показатель сытости - {self.satiety}; Эмоция - {self.emotion}; Уровень стресса - {self.stress}"]
        return self.arr

    # Дайте человеку поспать
    def sleep(self):
        self.stress -= 20

    # Занятие человека спортом
    def sport(self, type_sport):
        if type_sport == "Подтягивания":
            self.height += 1
        elif type_sport == "Бег":
            self.weight -= 1
        self.stress -= self.stress

    # Ранение человека
    def injure(self, type_of_injure):
        if type_of_injure == "Падение с низкой высоты" or type_of_injure == "Порез":
            self.health -= 5
            print(self.name, "больно")
        elif type_of_injure == "Отравление" or type_of_injure == "Лёгкая болезнь":
            self.health -= 10
            print(self.name, "плохо")
        elif type_of_injure == "Тяжёлая болезнь" or type_of_injure == "Большое падение с высоты":
            self.health -= random.randint(0, 50)
            print(self.name, "очень плохо.")
        elif type_of_injure == "Коронавирус":
            self.health -= random.randint(0, 100)
        else:
            print("Такого типа ранения нет в базе данных или не существует")
        self.emotion = "Печальный после ранения"
        self.stress += 10

    # Лечение человека
    def treatment(self, type_of_treatment):
        if type_of_treatment == "Принять таблетки":
            self.health += 10
        elif type_of_treatment == "Поход к врачу" or type_of_treatment == "Лечебный массаж":
            self.health += 20
        elif type_of_treatment == "Поход к частному врачу":
            self.health += 30
        else:
            print("Такого типа лечения нет в базе данных или не существует")
        self.emotion = "Радостный после лечния"
        self.stress -= 10

    # Питание человека
    def eating(self, type_of_food):
        if type_of_food == "Чай" or type_of_food == "Бутерброд":
            self.satiety += 5
        elif type_of_food == "Тортик" or type_of_food == "Каша" or type_of_food == "Макарончики":
            self.satiety += 10
        elif type_of_food == "Пельмешки" or type_of_food == "Пицца" or type_of_food == "Ланч":
            self.satiety += 20
        elif type_of_food == "Курочка" or type_of_food == "Жареная картошечка" or type_of_food == "Запечёная картошечка":
            self.satiety += 30
        else:
            print("Такого типа еды нет в базе данных или не существует")
        self.emotion = "Радостный, потому что покушал"
        self.stress -= 20

    # События, после которых меняется эмоция
    def events_emotion(self, event):
        if event == "Нашёл деьги" or event == "Получил зарплату" or event == "Поиграл" or event == "Расслабился":
            self.emotion = "Радость"
            self.stress -= 10
        elif event == "Потерял деньги" or event == "Умерла собака" or event == "Уволили с работы" or event == "Забыл что-то важное":
            self.emotion = "Грусть"
            self.stress += 10


# Создание Misha, который будте являться человеком, и задача некоторых параметров
Misha = Human()
# Время
time = 1
# Бесконечный цикл(почти)
while True:

    # Запрос на событие
    exec(input("Вводите событие >>"))

    # Изменение параметров со временем
    if Misha.height < 200:
        Misha.height += 1
    Misha.satiety -= 5
    Misha.stress -= 2

    # Проверка на определённые параметры, исправление некоторых параметров ,и события, связаные с человеком
    if Misha.health < 100:
        Misha.health += 1
    if Misha.health > 100:
        Misha.health = 100
    if time % 10 == 0:
        print(Misha.name, "отмечает день рождения!")
        Misha.age += 1
    if Misha.health < 1:
        print(Misha.name, "умер...")
        Misha.status = "Умер"
        print(Misha.name, "был хорошим человеком, а возможно и нет.")
        print("Конец")
        break
    if Misha.satiety < 70:
        print(Misha.name, "голодный")
    if Misha.satiety < 50:
        Misha.health -= 5
        print(Misha.name, "плохо без еды. Дайте ему еды!")
    if Misha.satiety < 20:
        Misha.health -= 10
        print("Срочно покормите", Misha.name, "!")
    if Misha.satiety > 100:
        Misha.satiety = 100
    if Misha.stress == 50:
        print(Misha.name, "испытывает стресс")
    if Misha.stress == 80:
        print(Misha.name, "испытывает большой стресс")
    if Misha.stress > 99:
        Misha.status = "Депрессия"
    if Misha.stress < 0:
        Misha.stress = 0

    # Выведение данных человека
    print(Misha.data())

    # Поток времени
    time += 1
