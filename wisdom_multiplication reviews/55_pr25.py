import numpy as np
import pandas as pd


def multiplication_check(x, y, length_check=False):
    return x * y == wisdom_multiplication(x, y, length_check)


def multiplication_check_list(start=10, stop=99, length_check=True):
    ans = [0, 0]
    for i in range(start, stop + 1):
        for j in range(start, stop + 1):
            ans[multiplication_check(i, j, length_check)] += 1
    print('''Правильных результатов: %d
Неправильных результатов: %d''' % (ans[1], ans[0]))


def wisdom_multiplication(x, y, length_check=True):
    x1, y1 = 100 - x, 100 - y
    first_half = str(100 - (x1 + y1))
    second_half = str(x1 * y1)
    second_half = '0' + second_half if len(
        second_half) < 2 and length_check else second_half
    return int(first_half + second_half)


def color(val):
    x = int(val[:2])
    y = int(val[3:])
    if multiplication_check(x, y):
        return 'color: green'
    elif multiplication_check(x, y, length_check=True):
        return 'color: yellow'
    else:
        return 'color: red'


a = np.arange(10, 100, 1)
tab = dict()
for i in a:
    tab[i] = []
    for j in a:
        tab[i].append(str(i) + 'x' + str(j))

pd.set_option('max_columns', 90)
pd.set_option('max_rows', 90)
pd.set_option('expand_frame_repr', False)
pd_tab = pd.DataFrame(data=tab, index=a)
pd_tab = pd_tab.style.applymap(color).render()

with open('55_tabl_umn.html', 'w') as file:
    file.write(pd_tab)
