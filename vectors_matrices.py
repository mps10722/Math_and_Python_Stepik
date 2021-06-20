import numpy as np
import pandas as pd

col = "animal"
row = "e"
df = pd.DataFrame({'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
                   'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
                   'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                   'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']},
                  index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

print(df['age'].count() * 1.0, df['age'].quantile(0.75), sep='\n')
