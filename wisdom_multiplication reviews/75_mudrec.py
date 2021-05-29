import pandas as pd

def color_negative_red(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    color = 'red' if val[1] == 1 else 'yellow' if val[1] == 2 else 'black'
    return 'color: %s' % color


def simple_multiplication2(x, y, length_check=True):
    a = 100 - x
    b = 100 - y
    c = str(a * b)
    d = a + b

    if length_check and len(c) == 1:
        c = '0' + c
        res1 = int(str(100 - d) + c)
        if x * y == res1:
            return res1, 2
    else:
        res1 = int(str(100 - d) + c)
        if x * y == res1:
            return res1, 1

    return res1, 0


# Создаем словарь для генерации таблицы
def ND(n):
    new_dict = {}  # Create a new empty dictionary
    for i in range(10, n):
        key = i
        # new_dict[key] =[i+j-10 for j in range(10,n)]
        new_dict[key] = [str(j) + 'x' + str(key) for j in
                         range(10, n)]  # list(range(10+1,n+1))
    return new_dict


# Генерируем таблицу произведений чисел "АхВ"
df = pd.DataFrame(ND(100), index=range(10, 100), columns=range(10, 100))


# Функция заменяет неправильные числа в таблице  нулями
def pr():
    for i in range(10, 100):
        for j in range(10, 100):
            tt = df[i][j]
            t1 = int(tt[0:2])
            t2 = int(tt[3:5])
            df[i][j] = simple_multiplication2(t1, t2)
            # print(t2*t1)
    return


# Варианты запуска программы
# multiplication_check_list()   # считаем правильные и неправильные числа
# df    # Исходная таблица
pr()  # Заменяем нулями неправильные числа
with open('75_output.html', 'w') as file:
    file.write(df.style.applymap(color_negative_red).format(lambda x: x[0]).render())
