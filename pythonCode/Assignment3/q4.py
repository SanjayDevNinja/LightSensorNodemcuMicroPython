import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = load_iris()

df = pd.DataFrame(data.data)
df['target'] = data.target
#print(df)

X_train, X_test, y_train, y_test = train_test_split(df.drop(['target'],axis='columns'), data.target, test_size=0.2)
model = RandomForestClassifier(n_estimators=30) #use 30 random forest
model.fit(X_train, y_train)
print("Model Score is:",model.score(X_test, y_test))