import pandas as pd
from sklearn.datasets import load_iris

data = load_iris()

df = pd.DataFrame(data.data)
df['target'] = data.target
print(df)