
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle 

dataset = pd.read_csv('finaldata.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 6].values
X1=dataset.iloc[:,:-1].values

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.000001, random_state = 0)
X_test1=X_test


labelencoder_X = LabelEncoder()
X[:, 5] = labelencoder_X.fit_transform(X[:, 5])
onehotencoder = OneHotEncoder()
X = onehotencoder.fit_transform(X).toarray()

X = X[:, 1:]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.000001, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

filename = 'new_model.sav'
pickle.dump(regressor , open(filename, 'wb'))

y_pred = regressor.predict(X_test)

for i in range(y_pred.size):
 data = pd.DataFrame([[X_test1[i][0],y_pred[i]]], columns=['Trained model','temperature'])
 data.to_csv('result.csv',mode='a', header=False)


print(y_pred)

plt.scatter(X1[:,2], y , color ='red')
plt.plot(X_test1[:,2], y_pred, color = 'blue')
plt.title('Results for Linear Regression')
plt.xlabel('Humidity')
plt.ylabel('Temperature')
plt.show()