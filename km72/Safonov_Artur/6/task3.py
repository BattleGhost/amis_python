def getnums(list):
    a = float(input("Введіть додатнє число a: "))
    n = int(input("Введіть ціле невідємне число n: "))
    list = [a, n]
    return list


def listtovar(list):
    a = list[0]
    n = list[1]
    return a, n


(a, n) = listtovar(getnums([]))


def power(a, n):
    a1 = a
    if n == 0:
        a = 1
    while n > 1:
        a *= a1
        n -= 1
        power(a, n)
    return a


print(str(a) + " в степені " + str(n) + " дорівнює", end =' ')
print(power(a,n))
