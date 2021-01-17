list = [int(i) for i in input("Вводите рост каждого человека в строю >>> ").split()]
print(list)
list.sort()
print(list)
height_human = int(input("Вводите рост человека, чьё место вы хотите найти >>> "))
print(list.index(height_human))
print(len(list) - list.index(height_human))
