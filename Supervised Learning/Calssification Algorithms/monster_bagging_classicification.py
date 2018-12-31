# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 11:08:27 2018

@author: Basha
"""

import os
import pandas as pd
from sklearn import tree
from sklearn import model_selection
from sklearn import ensemble #This is what we introduced here.

#returns current working directory 
os.getcwd()

#changes working directory
os.chdir("C:/data/monster")

monster_train = pd.read_csv("train.csv")

#EDA
monster_train.shape
monster_train.info()

monster_train1 = pd.get_dummies(monster_train, columns=['color'])
monster_train1.shape
monster_train1.info()
monster_train1.head(6)

X_train = monster_train1.drop(['type'], 1)
y_train = monster_train1['type']

#cv accuracy for bagged tree ensemble
dt_estimator = tree.DecisionTreeClassifier()

#Appy ensemble.BaggingClassificatier
#Base_Estimator = dt_estimator, n_estimators = 5(no. of trees)
bag_tree_estimator1 = ensemble.BaggingClassifier(base_estimator = dt_estimator, n_estimators = 4)
scores = model_selection.cross_val_score(bag_tree_estimator1, X_train, y_train, cv = 5)

#print(scores)
#print(scores.mean())
bag_tree_estimator1.fit(X_train, y_train)

#Alternative way with parameters and use GridSearchCV instead of cross_val_score
bag_tree_estimator2 = ensemble.BaggingClassifier(base_estimator = dt_estimator, n_estimators = 5, random_state=2017)
bag_grid = {'criterion':['entropy','gini']}
bag_grid_estimator = model_selection.GridSearchCV(bag_tree_estimator2, bag_grid, n_jobs=2)
bag_tree_estimator2.fit(X_train, y_train)

#.score gives the score on full train data
print(bag_tree_estimator2.score(X_train, y_train))

monster_csv_tst = pd.read_csv("C:/data/monster/test.csv")

monster_test1 = pd.get_dummies(monster_csv_tst, columns=['color'])
monster_test1.info

X_test = monster_test1
X_test.shape
X_test.info()

X_test['type'] = bag_tree_estimator2.predict(X_test)

os.getcwd()

X_test.to_csv("Submission_monster3.csv", columns=['id', 'type'], index=False)