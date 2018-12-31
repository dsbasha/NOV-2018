# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 15:48:03 2018

@author: Basha
"""

import pandas as pd
import os
from sklearn import tree, ensemble
from sklearn import model_selection

#changes working directory
os.chdir("C:/Data/monster")

monster_train = pd.read_csv("train.csv")
monster_train.shape
monster_train.info()

monster_test = pd.read_csv('test.csv')
monster_test.shape
monster_test.info()
monster_test.type = None

#it gives the same never of levels for all the categorical variables
monster = pd.concat([monster_train, monster_test])

#convert categorical columns to one-hot encoded columns
monster1 = pd.get_dummies(monster, columns=['color'])

monster1.shape
monster1.info()

monster2 = monster1.drop(['type'], axis=1, inplace=False)
monster2.shape

X_train = monster2[0:monster_train.shape[0]]
X_train.shape

X_train.info()
y_train = monster_train['type']

#create estimators for voting classifier
#Model 1
dt_estimator = tree.DecisionTreeClassifier(random_state=2019)

#Model 2
rf_estimator = ensemble.RandomForestClassifier(random_state=2019)

#Model 3
ada_estimator = ensemble.AdaBoostClassifier(random_state=2019)

voting_estimator = ensemble.VotingClassifier(estimators=[('dt', dt_estimator), ('rf', rf_estimator), ('ada', ada_estimator)])
voting_grid = {'dt__max_depth':[3,5,7], 'rf__n_estimators':[25], 'rf__max_features':[5,6], 'rf__max_depth':[5], 'ada__n_estimators':[25]}

grid_voting_estimator = model_selection.GridSearchCV(voting_estimator, voting_grid, cv=10, n_jobs=2)

grid_voting_estimator.fit(X_train, y_train)

print(grid_voting_estimator.grid_scores_)
print(grid_voting_estimator.best_score_)
print(grid_voting_estimator.best_params_)

print(grid_voting_estimator.score(X_train, y_train))


X_test = monster2[monster_train.shape[0]:]
X_test.shape
X_test.info()

monster_test['type'] = grid_voting_estimator.predict(X_test)

monster_test.to_csv('Monstor_Voting.csv', columns=['id','type'],index=False)