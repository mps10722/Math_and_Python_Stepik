# Python 3.8.5
import pandas as pd


# Умножение конкатенацией
def wisdom_multiplication(x, y, length_check=True):
    a = str(100 - ((100 - x) + (100 - y)))
    b = str((100 - x) * (100 - y))
    if length_check and len(b) == 1:
        b = '0' + b
    return int(a + b)


# Присвоение CSS стиля ячейке в зависимости от результата:
# Зелёный - ответ равен обычному умножению.
# Жёлтый - ответ равен обычному умножению если вставить 0.
# Красный - ответ неверный.
def color_check(val):
    y, x = (int(i) for i in val.split('x'))
    if wisdom_multiplication(x, y, False) == x * y:
        return 'color: %s' % 'green'
    elif wisdom_multiplication(x, y) == x * y:
        return 'color: %s' % 'yellow'
    else:
        return 'color: %s' % 'red'


# Формирование таблицы с маркировкой цветом результатов умножения
# методом конкатенации.
def table_check(start=10, stop=99):
    d = {x: [f"{y}x{x}" for y in range(start, stop + 1)] for x in
         range(start, stop + 1)}
    df = pd.DataFrame(data=d, index=range(start, stop + 1))
    st = df.style.applymap(color_check).render()
    with open('24_table_checked.html', 'w') as f:
        f.write(st)


table_check()
