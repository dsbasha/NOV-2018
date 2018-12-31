# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 12:21:21 2018

@author: Basha
"""

import pandas as pd
from sklearn import tree
import os

monster_csv = pd.read_csv("C:/data/monster/train.csv")
monster_csv.info
monster_csv.shape
monster_csv.describe()
monster_csv.head(10)

monster_train1 = pd.get_dummies(monster_csv, columns=['color'])
monster_train1.shape

X_train = monster_train1.drop(['type'], 1)
X_train.shape
X_train.info()

Y_train = monster_train1['type']

dt = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=7, min_samples_split=4)

dt.fit(X_train,Y_train)

monster_csv_tst = pd.read_csv("C:/data/monster/test.csv")

monster_test1 = pd.get_dummies(monster_csv_tst, columns=['color'])
monster_test1.info

X_test = monster_test1
X_test.shape
X_test.info()
X_test['type'] = dt.predict(X_test)

os.getcwd()
os.chdir("C:/data/monster")

X_test.to_csv("Submission_monster.csv", columns=['id', 'type'], index=False)