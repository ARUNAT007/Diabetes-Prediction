import numpy as np 
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
diabetes_dataset=pd.read_csv('C:/Users/HP/OneDrive/Desktop/Diabetes_Prediction/diabetes.csv')
diabetes_dataset.head()
diabetes_dataset.info()
diabetes_dataset.shape
diabetes_dataset.describe()
diabetes_dataset['Outcome'].value_counts()
diabetes_dataset.groupby('Outcome').mean()
X=diabetes_dataset.drop('Outcome',axis=1)
Y=diabetes_dataset['Outcome']
X = X.values
print(X)
print(Y)
scaler=StandardScaler()
scaler.fit(X)
standardized_data=scaler.transform(X)
print(standardized_data)
X=standardized_data
Y=diabetes_dataset['Outcome']
print(X)
print(Y)
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=2)
print(X.shape,X_train.shape,X_test.shape)
classifier=svm.SVC(kernel='linear')
classifier.fit(X_train,Y_train)
X_train_prediction=classifier.predict(X_train)
training_data_accuracy=accuracy_score(X_train_prediction,Y_train)
print('Accuracy score of the training data:',training_data_accuracy)
X_test_prediction=classifier.predict(X_test)
testing_data_accuracy=accuracy_score(X_test_prediction,Y_test)
print('Accuracy score of the testing data:',testing_data_accuracy)
input_data=(7,3,78,50,32,88,31,0.248,26)
input_data_as_numpy_array=np.asarray(input_data)
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
input_data_reshaped = input_data_reshaped[:, :-1]
std_data=scaler.transform(input_data_reshaped)
print(std_data)

prediction=classifier.predict(std_data)
print(prediction)

if(prediction[0]==0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')