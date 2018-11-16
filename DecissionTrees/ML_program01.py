import os
import pandas as pd 
from sklearn import tree #For Decissin Tree 
 
#Read Train Data file 
titanic_train = pd.read_csv("C:/Data/titanic/train.csv") 

titanic_train.shape #Not mandatory though!! 
titanic_train.info() #Not mandatory though!! 
titanic_train.describe() #Not mandatory though!! stats 
 
#Let's start the journey with non categorical and non missing data columns 
X_titanic_train = titanic_train[['Pclass', 'SibSp', 'Parch']] #X-Axis 
y_titanic_train = titanic_train['Survived'] #Y-Axis 

 
#Build the decision tree model 
dt = tree.DecisionTreeClassifier() 
dt.fit(X_titanic_train, y_titanic_train) 

 
#Predict the outcome using decision tree 
#Read the Test Data 
titanic_test = pd.read_csv("D:C:/Data/titanic/test.csv") 
X_test = titanic_test[['Pclass', 'SibSp', 'Parch']] 
#Use .predict method on Test data using the model which we built 
titanic_test['Survived'] = dt.predict(X_test)
os.getcwd() #To get current working directory 
titanic_test.to_csv("submission_Titanic.csv", columns=['PassengerId','Survived'], index=False) 
titanic_test.to_csv("C:/Data/titanic/submission_Titanic.csv", columns=['PassengerId','Survived'], index=False)
