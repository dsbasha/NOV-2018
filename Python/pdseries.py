import pandas as pd
ser1 = pd.Series(list1)
ser1

alphas = 'a,b,c,d,e,f,g,h,i'.split(',')
alphas
#data extraction
ser2=pd.Series(list1, index=alphas)
ser2.loc['f']
ser2.iloc[4]

ser3 = pd.Series(list1, index=range(1,10))
ser3

l2 = [3,4,5,7,9,23,345,67,89,67,34,89,67,2,3,4,8,56,34]

# Conditions
ser4 = pd.Series(l2)
ser4
ser4.loc[(ser4 > 40)]
ser4.loc[(ser4 > 40) & (ser4 < 70)]

#Functions
ser4.sort_values()

# Upper bound included in loc
ser4.loc[3:10]

# Upper bound excluded in iloc
ser4.iloc[3:10]
