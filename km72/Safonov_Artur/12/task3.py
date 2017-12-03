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
        список елементів. Використовується функцією
                    grouping(nums, onegrouplist, allgrouplist, i)

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


def grouping(nums, onegrouplist, allgrouplist, i):
    """
    Ця функція призначена для розбиття списку на групи з однаковими елементами

    Args:
        nums:           список, що розбивається
        onegrouplist:   список, в якому зберігається одна група елементів
        allgrouplist:   список, у який зберігаються всі списки елементів
        i:              число, що збільшується з кожним повторенням функції

    Return:
        список елементів. Використовується функцією
                    largestgroup(nums)

    Raises:
        OverflowError, TypeError, ValueError, RecursionError

    Examples:
        [1, 1, 1, 2, 3, 3, 4, 4 , 5 , 4, 4, 5]
        [[1, 1, 1], [2], [3, 3], [4, 4], [5], [4, 4], [5]]
    """
    if len(nums) > i:
        if nums[i] == nums[0]:
            onegrouplist.append(nums[i])
            i += 1
            return grouping(nums, onegrouplist, allgrouplist, i)
        else:
            nums = nums[len(onegrouplist):]
            allgrouplist.append(onegrouplist)
            onegrouplist = []
            return grouping(nums, onegrouplist, allgrouplist, 0)
    allgrouplist.append(onegrouplist)
    return allgrouplist


result = grouping(strlist, [], [], 0)


def largestgroup(nums):
    """
    Ця функція призначена для визначення групи, в якій найбільше елементів

    Args:
        nums:       список, що перевіряється

    Return:
        список елементів. Виводиться користувчу

    Raises:
        OverflowError, TypeError, ValueError, RecursionError

    Examples:
        [[1, 1, 1], [2], [3, 3], [4, 4], [5], [4, 4], [5]]
        [1, 1, 1]
    """
    if len(nums) > 1:
        if len(nums[0]) > len(nums[1]):
            del nums[1]
        else:
            del nums[0]
        largestgroup(nums)
    return nums[0]


if len(largestgroup(result)) > 1:
    print("Найбільша група чисел - " + str(len(largestgroup(result))) +
          " числа: " + str(largestgroup(result)))
else:
    print("Всі елементи розташовані по одному")
