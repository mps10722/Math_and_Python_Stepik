import pandas as pd


# Функция выполняет "умножение мудреца" с проверкой длины или без
def wisdom_multiplication(x, y, length_check=True):
    s1 = 100 - x + 100 - y
    s2 = 100 - s1
    s3 = str((100 - x) * (100 - y))
    if length_check and len(s3) < 2:
        s3 = '0' + s3
    return int(str(s2) + s3)


# Функция проверяет результат "умножения мудреца" и обычное умножение
def multiplication_check(x, y, length_check=True):
    return wisdom_multiplication(x, y, length_check) == x * y


# Функция используется для покраски ячеек, она достает из словаря colors
# значение цвета для каждой ячейки
def colorize(s):
    global colors
    return f'background-color: {colors[s]}'


start = 10
end = 100

colors = dict()

data = []

# В этом цикле происходит проверка умножения, заполнение таблицы и заполнение
# словаря colors
for i in range(start, end):
    dataColumn = []
    for g in range(start, end):
        if multiplication_check(i, g, length_check=False):
            colors[f'{i}x{g}'] = 'green'
        elif multiplication_check(i, g, length_check=True):
            colors[f'{i}x{g}'] = 'yellow'
        else:
            colors[f'{i}x{g}'] = 'red'
        dataColumn.append(f'{i}x{g}')
    data.append(dataColumn)

# Создание таблицы
df = pd.DataFrame(data, index=range(start, end), columns=range(start, end))

# Применение цветов и сохранение результата в html
with open('wisdom check table.html', 'w') as fout:
    fout.write(df.style.applymap(colorize).render())
