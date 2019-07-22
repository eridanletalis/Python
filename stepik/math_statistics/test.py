import pandas as pd
import numpy as np

s1 = np.arange(10, 50, 5)
s2 = np.arange(50, 10, -5)
df = pd.DataFrame({"first": s1, "second": s2}, index=['v' + str(i) for i in range(s1.size)])
print(df[df['first'] >= 20])