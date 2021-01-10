country_cities = {}
city_country = {}
for i in range(int(input("Введите количество стран\n"))):
    country = input("Введите страну\n")
    cities = input("Вводите города\n")
    country_cities[country] = cities
    for i in cities:
        city_country[i] = country
for i in range(int(input("Введите количество городов, которые вы хотите найти\n"))):
    search_request = input("Вводите город\n")
    if search_request in city_country:
        print(city_country[search_request])
    elif search_request in country_cities:
        print("Это не город, это страна. Вот её города:", country_cities[search_request])
    else:
        print("Такого города не существует!")