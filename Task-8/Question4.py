#QUESTION-4

import pandas as pd

ser = pd.Series(['amrita','school','of','engineering'])
for i in range(len(ser)):
    ser[i]=ser[i].capitalize()
    print(ser[i],end=" ")