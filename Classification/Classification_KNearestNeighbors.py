import numpy as np
from sklearn import preprocessing, model_selection, neighbors
import pandas as pd

df = pd.read_csv('breast-cancer-wisconsin.data.txt')
df.replace('?',-99999, inplace=True)
df.drop(['id'], 1, inplace=True)

X = np.array(df.iloc[:, 0:-1])
y = np.array(df.iloc[:, -1])


print(X)
print("**************")
print(y)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print(accuracy)

example_measures= np.array([[4,2,1,1,1,2,3,2,1]])
prediction= clf.predict(example_measures)
print(prediction)
