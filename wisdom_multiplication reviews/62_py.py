#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


def multiplication_check_list(start=10, stop=99):
    dx = []
    for x in range(start, stop + 1):
        dy = []
        for y in range(start, stop + 1):
            d1, d2 = 100 - ((100 - x) + (100 - y)), (100 - x) * (100 - y)
            dy.append((f'{x}x{y}',
                       (int(f'{d1}{d2}') == x * y) + (d1 * 100 + d2 == x * y)))
        dx.append(dy)
    return dx


def st_colors(s):
    return 'background-color:' + colors[s[1]]


start = 10
stop = 99
data = multiplication_check_list(start, stop)
r = range(start, stop + 1)
colors = ['white', 'yellow', 'green']

df = pd.DataFrame(data, r, r)

# In[2]:

df.applymap(lambda x: x[0])
df.style.applymap(st_colors)

with open('62_file.html', 'w') as f:
    f.write(df.style.applymap(st_colors).render())
# In[ ]:
