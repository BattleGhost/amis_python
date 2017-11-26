def inputing():
    """
    Ця функція призначена для введення даних користувачем

    Return:
        Результат - список елементів. Використовується функцією
        notempty(nums, filled)

    Raises:
        OverflowError

    Examples:
        Введіть цілі числа: 21312 123 123
        ['21312', '123', '123']
    """
    nums = (input("Введіть цілі числа: ")).split()
    return nums


def notempty(nums, filled):
    """
    Ця функція призначена для перевірки списку на наявність елементів

    Args:
        nums:   список, що перевіряється
        filled: список, в якому наявні елементи

    Return:
        Результат - список елементів. Використовується функцією
         checking(nums, newnums)

    Raises:
        OverflowError, TypeError

    Examples:
        Введіть цілі числа: 21312 123 123
        ['21312', '123', '123']

        Введіть цілі числа:
        Введіть цілі числа: 1 2 3
        ['1', '2', '3']
    """
    if len(nums) < 1:
        nums = inputing()
        notempty(nums, filled)
    else:
        filled.append(nums)
    return filled[0]


def checknum(num, numlist):
    """
    Ця функція призначена для перевірки чи є елемент цілим числом

    Args:
        num:   елемент, що перевіряється
        numlist: список, в якомий заносяться 0 або 1 згідно з тим,
         чи цифра знакодиться в елементі

    Return:
        Результат - 1 - якщо елемент - ціле число, 0 - якшо ні.
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

        adw
        0

        14f
        0
    """
    if len(num) > 1 and '-' in num:
        num = num[1:]
        if '-' in num:
            numlist.append(0)
    if len(num) > 1 and num[0] == "0":
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
    Ця функція призначена для перевірки чи всі елементи списку числа

    Args:
        nums:   список, що перевіряється
        newnums: список, в якому знаходяться лише числа

    Return:
        Результат - список елементів. Використовується функцією
        strtoint(nums, intnums)

    Raises:
        OverflowError, TypeError, RecursionError

    Examples:
        ['1', '324', 'g3', '34h', '123']
        g3 - не ціле число, введіть замість нього ціле число: 5
        34h - не ціле число, введіть замість нього ціле число: f
        f - не ціле число, введіть замість нього ціле число: 24
        ['1', '324', '5', '24', '123']
    """
    if len(nums) != 0:
        if checknum(nums[0], []) == 0:
            result = input(str(nums[0]) + " - не ціле число,"
                                          " введіть замість"
                                          " нього ціле число: ")
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
        reverse(nums, revnums)

    Raises:
        OverflowError, TypeError, ValueError, RecursionError

    Examples:
        ['1', '324', '5', '24', '123']
        [1, 324, 5, 24, 123]
    """
    if len(nums) != 0:
        nums[0] = int(nums[0])
        intnums.append(nums[0])
        nums.remove(nums[0])
        strtoint(nums, intnums)
    return intnums


strlist = strtoint(listchecking, [])


def reverse(nums, revnums):
    """
    Ця функція призначена для виведення списку у зворотній послідовності

    Args:
        nums:       список з прямою послідовністью
        revnums:    список з оберненою послідовністью

    Return:
        Результат - список елементів. Виводиться користувачу

    Raises:
        OverflowError, TypeError, RecursionError

    Examples:
        [1, 324, 5, 24, 123]
        [123, 24, 5, 324, 1]

        [13, 15, 2, 11, 0, -1, 4]
        [4, -1, 0, 11, 2, 15, 13]
    """
    if len(nums) > 0:
        revnums.insert(0, nums[0])
        nums = nums[1:]
        reverse(nums, revnums)
    return revnums


print(reverse(strlist, []))
