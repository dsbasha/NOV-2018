# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 22:21:03 2018

@author: Basha
"""
import pandas as pd
from sklearn import tree
import io
import pydot #if we need to use any external .exe files....
import os
os.chdir("C:/data/")
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

titanic_train = pd.read_csv("C:/data/train.csv")
titanic_train.shape
titanic_train.info()
titanic_train.describe()

#Transformation of non numneric cloumns to 1-Hot Encoded columns
#There is an exception with the Pclass. Though it's co-incidentally a number column but it's a Categoric column(Even common-sence wise).
#Transform categoric to One hot encoding using get_dummies
titanic_train1 = pd.get_dummies(titanic_train, columns=['Pclass', 'Sex', 'Embarked'])
titanic_train1.shape
titanic_train1.head(10)
titanic_train1.info()
titanic_train1.describe()

#now the drop non numerical columns where we will not be applying logic. Something like we will not apply logic on names, passengerID ticket id etc...
X_train = titanic_train1.drop(['PassengerId','Age','Cabin','Ticket', 'Name','Survived'], 1)
X_train.info()
y_train = titanic_train['Survived']
X_train.info()
dt = tree.DecisionTreeClassifier(criterion = 'entropy')

#.fit builds the model. In this case the model building is using Decission Treee Algorithm
dt.fit(X_train,y_train)

#visualize the decission tree
dot_data = io.StringIO()  
tree.export_graphviz(dt, out_file = dot_data, feature_names = X_train.columns)
#graph = pydot.graph_from_dot_data(dot_data.getvalue())
#graph[0].write_pdf("DT.pdf")

#predict the outcome using decission tree
titanic_test = pd.read_csv("C:/data/test.csv")
titanic_test.shape

#Fill missing data of Test(Fare)
titanic_test.info() #Found that one row has Fare = null in test data. Instead of dropping this column, let's take the mean of it.
titanic_test.Fare[titanic_test['Fare'].isnull()] = titanic_test['Fare'].mean()

#Now apply same get_dummies and drop columns on test data as well like above we did for train data
titanic_test1 = pd.get_dummies(titanic_test, columns=['Pclass', 'Sex', 'Embarked'])
X_test = titanic_test1.drop(['PassengerId','Age','Cabin','Ticket', 'Name'], 1)

#Apply the model on future/test data
titanic_test['Survived'] = dt.predict(X_test)
os.getcwd()

titanic_test.to_csv("Submission_Attempt2.csv", columns=['PassengerId', 'Survived'], index=False)
