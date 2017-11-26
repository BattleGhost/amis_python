def inputing():
    """
    Ця функція призначена для введення даних користувачем

    Return:
        Результат - список елементів. Використовується функцією
        notempty(nums, filled)

    Raises:
        OverflowError

    Examples:
        Введіть 2 цілі числа: 21312 123
        ['21312', '123']
    """
    nums = (input("Введіть 2 цілі додатні числа: ")).split()
    return nums


def notempty(nums, filled):
    """
    Ця функція призначена для перевірки списку на кількість елементів

    Args:
        nums:   список, що перевіряється
        filled: список, в якому наявні 2 елементи

    Return:
        Результат - список елементів. Використовується функцією
         checking(nums, newnums)

    Raises:
        OverflowError, TypeError

    Examples:
        Введіть 2 цілі числа: 21312 123 123
        Введіть 2 цілі числа: 234
        Введіть 2 цілі числа: 1 4
        ['1', '4']

        Введіть цілі числа:
        Введіть цілі числа: 1 2
        ['1', '2']
    """
    if (len(nums) < 2) or (len(nums) > 2):
        nums = inputing()
        notempty(nums, filled)
    else:
        filled.append(nums)
    return filled[0]


def checknum(num, numlist):
    """
    Ця функція призначена для перевірки чи є елемент цілим додатнім числом

    Args:
        num:   елемент, що перевіряється
        numlist: список, в якомий заносяться 0 або 1 згідно з тим,
         чи цифра знакодиться в елементі

    Return:
        Результат - 1 - якщо елемент - ціле додатнє число, 0 - якшо ні.
        Використовується функцією checking(num, newnums)

    Raises:
        OverflowError, RecursionError

    Examples:
        4124
        1

        -123
        1

        12-4
        0

        024
        0

        adw
        0

        14f
        0
    """
    if len(num) > 1 and num[0] == "0":
        numlist.append(0)
    if num == "0":
        numlist.append(0)
    if len(num) != 0:
        if num[0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            numlist.append(1)
            num = num[1:]
        else:
            numlist.append(0)
            num = num[1:]
        checknum(num, numlist)
    if 0 in numlist:
        return 0
    else:
        return 1


def checking(nums, newnums):
    """
    Ця функція призначена для перевірки чи всі елементи списку додатні числа

    Args:
        nums:   список, що перевіряється
        newnums: список, в якому знаходяться лише додатні числа

    Return:
        Результат - список елементів. Використовується функцією
        strtoint(nums, intnums)

    Raises:
        OverflowError, TypeError, RecursionError

    Examples:
        ['g3', '34h']
        g3 - не ціле число, введіть замість нього ціле число: 5
        34h - не ціле число, введіть замість нього ціле число: f
        f - не ціле число, введіть замість нього ціле число: 24
        ['5', '24']
    """
    if len(nums) != 0:
        if checknum(nums[0], []) == 0:
            result = input(str(nums[0]) + " - не ціле додатнє число,"
                                          " введіть замість"
                                          " нього ціле додатнє число: ")
            nums.remove(nums[0])
            nums.insert(0, result)
        else:
            newnums.append(nums[0])
            nums = nums[1:]
        checking(nums, newnums)
    return newnums


listchecking = checking(notempty(inputing(), []), [])


def strtoint(nums, intnums):
    """
    Ця функція призначена для зміни типу всіх елементів списку з str на int

    Args:
        nums:       список, тип елементів якого змінюється
        intnums:    список, всі елементи якого мають тип int

    Return:
        Результат - список елементів. Використовується функцією
        gcd(x, y)

    Raises:
        OverflowError, TypeError, ValueError, RecursionError

    Examples:
        ['1', '324']
        [1, 324]
    """
    if len(nums) != 0:
        nums[0] = int(nums[0])
        intnums.append(nums[0])
        nums.remove(nums[0])
        strtoint(nums, intnums)
    return intnums


strlist = strtoint(listchecking, [])


def gcd(x, y):
    """
    Ця функція призначена для знаходження НСД 2 чисел

    Args:
        x:  число, НСД якого з другим знаходиться
        y:  число, НСД якого з першим знаходиться

    Return:
        Результат - число. Виводиться користувачу

    Raises:
        OverflowError, TypeError, ValueError, RecursionError

    Examples:
        ['1', '324']
        1

        ['500', '420']
        20
    """
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


print("НСД цих чисел = " + str(gcd(strlist[0], strlist[1])))
