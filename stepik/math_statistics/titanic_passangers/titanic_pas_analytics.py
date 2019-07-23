import pandas as pd

s = pd.Series([int(i) for i in input().split()])
a = s.mean()

print(a)