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

#oob scrore is computed as part of model construction process
dt_estimator = tree.DecisionTreeClassifier()
ada_estimator = ensemble.AdaBoostClassifier(base_estimator = dt_estimator, random_state = 2017)
ada_grid = {'n_estimators':[10,15,20], 'learning_rate':[0.01,0.02,0.8], 'base_estimator__max_depth':[3]}

grid_ada_estimator = model_selection.GridSearchCV(ada_estimator, ada_grid, cv=10, n_jobs=2)

#print(scores)
#print(scores.mean())
grid_ada_estimator.fit(X_train, y_train)

#.score gives the score on full train data
print(grid_ada_estimator.score(X_train, y_train))

monster_csv_tst = pd.read_csv("C:/data/monster/test.csv")

monster_test1 = pd.get_dummies(monster_csv_tst, columns=['color'])
monster_test1.info

X_test = monster_test1
X_test.shape
X_test.info()

X_test['type'] = grid_ada_estimator.predict(X_test)

os.getcwd()

X_test.to_csv("Submission_monster4.csv", columns=['id', 'type'], index=False)