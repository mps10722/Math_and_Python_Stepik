import pandas as pd


def color_negative_red(val):
    x, y = val.split('*')
    x = int(x)
    y = int(y)
    a = 100 - x
    b = 100 - y
    s = a + b
    rest = str(a * b)
    color = 'red' if (str(100 - s) + rest == str(x * y)) else 'black'
    return 'color: %s' % color


df = pd.DataFrame()
for i in range(10, 100):
    df[str(i)] = [f'{j}*{i}' for j in range(10, 100)]

s = df.style.applymap(color_negative_red)
with open('38_mudrec.html', 'w') as f:
    f.write(s.render())
