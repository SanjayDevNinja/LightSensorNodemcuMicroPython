import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

data = load_iris()

 
#Flower Representation in matplotLib
flowerMatplotMarkers = ["ro","g^","b1"]

for i in range(3):
  plt.title(data.target_names[i])  
  plt.plot(i, i, flowerMatplotMarkers[i])
  plt.show()
  
  
  
