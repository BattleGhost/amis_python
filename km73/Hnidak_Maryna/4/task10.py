'''
Умова: Шахова королева рухається по горизонталі, по вертикалі або по діагоналі
на будь-яку кількість клітин. Дано координати двох клітин шахової дошки.
Визначити, чи може королева перейти з першої клітини у другу за один хід.
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер
рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два
числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в
іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
'''
a = int(input("Введіть номер рядку, де розташувана королева - "))
b = int(input("Введіть номер стовпчика, де розташувана королева - "))
c = int(input("Введіть номер рядку,куди королева повинна перейти - "))
d = int(input("Введіть номер стовпчика,куди королева повинна перейти - "))
if (a<1 or a>8) or (b<1 or b>8) or (c<1 or c>8) or (d<1 or d>8):
    answer = "NO"
elif (abs(a-c)==abs(b-d)) or (a==c or b==d):
    answer = "YES"
else:
    answer = "NO"
print (answer)