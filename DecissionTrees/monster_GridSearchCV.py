# -*- coding: utf-8 -*-
"""
Model tuning
@author: Basha
"""
import pandas as pd
from sklearn import tree
from sklearn import model_selection
import os

#os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
#returns current working directory
os.getcwd()

#changes working directory
os.chdir("C:/data/monster")
monster_csv = pd.read_csv("train.csv")
print(type(monster_csv))

#EDA
monster_csv.shape
monster_csv.info()

#Apply one hot encoding
monster_train1 = pd.get_dummies(monster_csv, columns= ['color'])
monster_train1.shape
monster_train1.info()
X_train = monster_train1.drop(['type'], 1)
y_train = monster_train1['type']

#Section 1A
dt1 = tree.DecisionTreeClassifier()
dt1.fit(X_train,y_train)

#Apply K-fold technicque and find out the Cross Validation(CV) score.
cv_scores1 = model_selection.cross_val_score(dt1, X_train, y_train, cv=10)
print(cv_scores1) #Return type is a [List] of score
print(cv_scores1.mean()) #Find out the mean of CV scores

#Section 1B
print(dt1.score(X_train,y_train))

#Section 2A
#tune model manually by passing differnt values for decision tree arguments
dt2 = tree.DecisionTreeClassifier(max_depth=4, random_state=1) #Here we passed max-depth as argument to the tree
dt2.fit(X_train,y_train)
cv_scores2 = model_selection.cross_val_score(dt2, X_train, y_train, cv=10)
print(cv_scores2) #Return type is a [List] of scores
print(cv_scores2.mean())

#Section 2B
print(dt2.score(X_train,y_train))
#Automate model tuning process. Use Grid search method
dt3 = tree.DecisionTreeClassifier()
param_grid = {'max_depth':[5,7,10], 'min_samples_split':[2,4,5], 'criterion':['gini','entropy']} 
print(param_grid)

#max_depth means: Max deapth of the tree to child nodes
#min_samples_split means: If you notice the tree nodes, there is some thing called sample in each node. This is what it is referring to min sample split
dt3_grid = model_selection.GridSearchCV(dt3, param_grid, cv=10)
#dt3_grid = model_selection.GridSearchCV(dt3, param_grid, cv=10, n_jobs=5)
dt3_grid.fit(X_train, y_train)
print(dt3_grid.grid_scores_) #You may get DeprecationWarning

#print(dt3_grid.cv_results_) #New version
final_model = dt3_grid.best_estimator_ #This is the estimator of max_deapth and min_sample_split combination
print(dt3_grid.best_score_)
print(dt3_grid.best_params_)# get best score parameters

#.score gives the score on full train data
print(dt3_grid.score(X_train, y_train))

monster_csv_tst = pd.read_csv("C:/data/monster/test.csv")

monster_test1 = pd.get_dummies(monster_csv_tst, columns=['color'])
monster_test1.info

X_test = monster_test1
X_test.shape
X_test.info()

X_test['type'] = dt3_grid.predict(X_test)

os.getcwd()

X_test.to_csv("Submission_monster2.csv", columns=['id', 'type'], index=False)