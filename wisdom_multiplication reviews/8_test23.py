import pandas

# увеличения лимита отображаемых строк
pandas.set_option("display.max_rows", 10000)

# DataFrame создается пустой
df = pandas.DataFrame(columns=['amount'])

# устанавливается диапозон вывода строк
start = 10
stop = 99


# функция
# Визуально отмечает те ячейки таблицы, где работает "схема мудреца"
# Зеленный - те где достаточно схемы без проверки на разделитель 0 внутри
# Красный - те где требуется проверка на 0
def color_red(val):
    x = int(val[0:2])
    y = int(val[3:5])
    p = str((100 - x) * (100 - y))

    if len(p) == 1:
        color = 'red'
    else:
        color = 'green'

    return 'color: %s' % color


# в DataFrame записываются значения строк от 10 до 99
k = 0

for j in range(start, stop + 1):
    for i in range(start, stop + 1):
        df.loc[k, 'amount'] = str(j) + 'x' + str(i)
        k = k + 1

# в DataFrame выделяет цветом
s = df.style.applymap(color_red).render()

# выводит строки
with open('8_test23 - Jupyter Notebook.html', 'w') as file:
    file.write(s)
