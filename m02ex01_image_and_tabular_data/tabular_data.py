import pandas as pd
import numpy as np

df = pd.read_csv('m02ex01_image_and_tabular_data/data/advertising.csv')
print(df.head())

data = df.to_numpy()
sales = data[:, 3]
tv = data[:, 0]
newspaper = data[:, 2]

print('15)', sales.max(), sales.argmax())
print('16)', tv.mean())
print('17)', (sales >= 20).sum())
print('18)', data[sales >= 15][:, 1].mean())
print('19)', data[newspaper >= newspaper.mean()][:, 3].sum())

a = sales.mean()
scores = np.where(sales > a, "Good", np.where(sales < a, "Bad", "Average"))
print('20)',scores[7:10])

sales1 = abs(sales - a)
b = sales[sales1.argmin()]
scores = np.where(sales > b, "Good", np.where(sales < b, "Bad", "Average"))
print('21)', scores[7:10])