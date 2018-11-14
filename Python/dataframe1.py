#Data Frames1 
#Python is case sensitive 
import pandas as pd 
print(pd.__version__) 
titanic_train_csv_csv = pd.read_csv("D:/Data Science/Data/titanic_train_csv_csv.csv") 
print(type(titanic_train_csv)) 

#explore the dataframe 
titanic_train_csv.shape #No of rows and Column 
#Data Type and nullable/non-nullable
titanic_train_csv.info()  
#Gives statistical information 
titanic_train_csv.describe() 
 
#access column/columns of a dataframe 
titanic_train_csv['Sex'] 
titanic_train_csv['Fare'] 
titanic_train_csv.Sex 
titanic_train_csv.Fare 
temp = titanic_train_csv[['Survived','Fare', 'Embarked']] 
print(type(temp)) 
 
#access rows of a data frame 
titanic_train_csv.iloc[855] #ith record from DF
 
titanic_train_csv[10:20]
titanic_train_csv.iloc[10:20] 

titanic_train_csv[885:891] 
titanic_train_csv.iloc[885:891] 
 
#Get me top n records 
titanic_train_csv.head(6) 
#Get me bottom n records 
titanic_train_csv.tail(6) 

 
#access both rows and columns of a dataframe 
titanic_train_csv.iloc[10:20] 

 
#If you wanted to access by column name then use .loc 
titanic_train_csv.loc[10:20,'Name'] 

#conditional access of dataframe 
titanic_train_csv.loc[titanic_train_csv.Sex == 'female', 'Sex'] 
titanic_train_csv.loc[titanic_train_csv.Sex == 'female', 'Name'] 
 
#grouping data in data frames 
titanic_train_csv.groupby(['Pclass']).size() 
titanic_train_csv.groupby(['Pclass', 'Sex']).size() 
titanic_train_csv.groupby(['Embarked', 'Pclass']).mean() 

titanic_train_csv.groupby(['Embarked', 'Pclass']).mean()['Fare'] 
