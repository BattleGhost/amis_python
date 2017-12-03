def inputing(msg):
    """
    Ця функція призначена для введення даних користувачем

    Args:
        msg:    рядок, що відобразиться при показі підказки до введення даних

    Return:
        список елементів. Використовується функцією
                    notempty(nums, filled)

    Raises:
        OverflowError

    Examples:
        Введіть цілі числа: 21312 123 123
        ['21312', '123', '123']
    """
    nums = (input(msg + "Введіть натуральні числа: ")).split()
    return nums


def notempty(nums, filled):
    """
    Ця функція призначена для перевірки списку на кількість елементів

    Args:
        nums:   список, що перевіряється
        filled: список, в якому наявні елементи

    Return:
        список елементів. Використовується функцією
                    checking(nums, newnums)

    Raises:
        OverflowError, TypeError

    Examples:
        Введіть натуральні числа: 21312 123 123
        ['21312', '123', '123']

        Введіть натуральні числа:
        У списку менше 2 елементів. Введіть натуральні числа: 235 53
        ['235', '53']
    """
    if len(nums) < 1:
        nums = inputing("Список порожній. ")
        notempty(nums, filled)
    else:
        filled.append(nums)
    return filled[0]


def checknum(num, numlist):
    """
    Ця функція призначена для перевірки чи є елемент натуральним числом

    Args:
        num:   елемент, що перевіряється
        numlist: список, в якомий заносяться 0 або 1 згідно з тим,
         чи цифра знакодиться в елементі

    Return:
        1 - якщо елемент - ціле число, 0 - якшо ні.
        Використовується функцією checking(num, newnums)

    Raises:
        OverflowError, RecursionError

    Examples:
        4124
        1

        -123
        0

        12-4
        0

        adw
        0

        14f
        0

        0
        0
    """
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
        список елементів. Використовується функцією
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
        if checknum(nums[0], []) == 0 or nums[0] == "0" or nums[0][0] == "0":
            result = input(str(nums[0]) + " - не натуральне число,"
                                          " введіть замість"
                                          " нього натуральне число: ")
            nums.remove(nums[0])
            nums.insert(0, result)
        else:
            newnums.append(nums[0])
            nums = nums[1:]
        checking(nums, newnums)
    return newnums


listchecking = checking(notempty(inputing(""), []), [])


def strtoint(nums, intnums):
    """
    Ця функція призначена для зміни типу всіх елементів списку з str на int

    Args:
        nums:       список, тип елементів якого змінюється
        intnums:    список, всі елементи якого мають тип int

    Return:
        список елементів. Використовується функціями
                    maximum(nums) і listfornumber(nums, newnums, n)

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


def listfornumber(nums, newnums, n):
    """
    Ця функція призначена для створення списку в якому буде знаходитись другий
    максимум

    Args:
        nums:       список, який буде змінюватись в подальшому
        newnums:    список, що не буде змінюватись в подальшому і в якому
                    буде знаходитись кількість максимумів
        n:          число, що збільшується на 1 з кожним повторенням функції

    Return:
        список елементів. Використовується функцією
        amountofmax(nums, num, amount)

    Raises:
        OverflowError, TypeError, RecursionError

    Examples:
        [1, 2, 3, 4, 5]
        [1, 2, 3, 4, 5]
    """
    if len(newnums) != len(nums):
        newnums.append(nums[n])
        n += 1
        listfornumber(nums, newnums, n)
    return newnums


def maximum(nums):
    """
    Ця функція призначена для знаходження максимального елемента списку

    Args:
        nums:       список, в якому буде знаходитись максимум

    Return:
        число, використовється функцією
                    amountofmax(nums, num, amount)

    Raises:
        OverflowError, TypeError, ValueError, RecursionError

    Examples:
        [42, 14, 21, 8, 3]
        42

        [1, 325, 2, 6, 7]
        325
    """
    if len(nums) > 1:
        if nums[0] > nums[1]:
            del nums[1]
        else:
            del nums[0]
        maximum(nums)
    return nums[0]


def amountofmax(nums, num, amount):
    """
    Ця функція призначена для знаходження кількості максимальних елементів

    Args:
        nums:       список, в якому буде знаходитись кількість елементів
        num:        елемент, кількість якого буде знаходитись
        amount:     кількість цих елементів

    Return:
        число, виводиться користувачу

    Raises:
        OverflowError, TypeError, RecursionError

    Examples:
        [42, 42, 14, 42, 21, 8, 3], 42, 0
        3

        [1, 325, 2, 6, 7, 7, 7, 7, 325, 7]
        2
    """
    if num in nums:
        amount += 1
        nums.remove(num)
        return amountofmax(nums, num, amount)
    return amount


result = amountofmax(listfornumber(strlist, [], 0), maximum(strlist), 0)
print("Кількість елементів, рівних максимуму = " + str(result))
