import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

data = load_iris()

print(dir(data))
#print(data.data)
print(data.feature_names)
print(data.target_names[0])
print(data.target)


