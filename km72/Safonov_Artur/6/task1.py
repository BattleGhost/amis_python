def getcoords(list):
    x1 = float(input("Введіть координату х першої точки: "))
    y1 = float(input("Введіть координату y першої точки: "))
    x2 = float(input("Введіть координату х другої точки: "))
    y2 = float(input("Введіть координату y другої точки: "))
    list = [x1, y1, x2, y2]
    return list


def listtovar(list):
    x1 = list[0]
    y1 = list[1]
    x2 = list[2]
    y2 = list[3]
    return x1, y1, x2, y2


(x1, y1, x2, y2) = listtovar(getcoords([]))


def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y1 - y2) ** 2) ** 0.5


print("Відстань між точками (х1;у1) і (х2;у2) дорівнює", end=' ')
print(distance(x1, y1, x2, y2))