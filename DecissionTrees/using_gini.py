# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 19:49:22 2018

@author: Basha
"""

import pandas as pd
from sklearn import tree
import os

titanic_csv = pd.read_csv("C:/data/train.csv")
titanic_csv.info
titanic_csv.shape
titanic_csv.describe()
titanic_csv.head(10)

titanic_train1 = pd.get_dummies(titanic_csv, columns=['Pclass', 'Sex', 'Embarked'])
titanic_train1.shape

X_train = titanic_train1.drop(['Age','Cabin','Ticket', 'Name','Survived'], 1)
X_train.shape
X_train.info()

Y_train = titanic_train1['Survived']

dt = tree.DecisionTreeClassifier(criterion = 'gini', max_depth=10, min_samples_split=5)

dt.fit(X_train,Y_train)

titanic_csv_tst = pd.read_csv("C:/data/test.csv")
titanic_csv_tst.Fare[titanic_csv_tst['Fare'].isnull()] = titanic_csv_tst['Fare'].mean()

titanic_test1 = pd.get_dummies(titanic_csv_tst, columns=['Pclass', 'Sex', 'Embarked'])
titanic_test1.info

X_test = titanic_test1.drop(['Age','Cabin','Ticket', 'Name'], 1)
X_test.shape
X_test.info()
X_test['Survived'] = dt.predict(X_test)

os.getcwd()
os.chdir("C:/data/")

X_test.to_csv("Submission_Attempt5.csv", columns=['PassengerId', 'Survived'], index=False)
