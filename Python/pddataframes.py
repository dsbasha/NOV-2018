#Data Frames and Tables - creating using Pandas Series
import pandas as pd

s1=pd.Series([1,2,3,4,5,], name="Eid")
s2=pd.Series(["Markella","Sindhu","Anjali","Sakshi","Anushka"],name="Ename")
s3=pd.Series([34232,34534,56789,78906,908764],name="sal")
empdf = pd.concat([s1,s2,s3],axis=1)
type(empdf)
empdf

c1=list(s1)
c2=list(s2)
c3=list(s3)

empdict={"EmpID":c1, "Name":c2, "Sal":c3}

emp2df = pd.DataFrame(empdict)

emp2d


#importing data from external sources using csv
#File path, Filename, extention
df_stores=pd.read_csv("C:/Basha/stores/stores.csv")

#shape of data - Display rows and columns
s = df_stores.shape

nrows = s[0]
ncols = s[1]

#Names of the columns
df_stores.columns

#list containing column names
list[df_stores.colums]

#Data types -output is pandas seeries. Loc is column name and values are data types. str renamed as Object
df_stores.dtypes

# Get a count of numbers, strings, dates and bool

df_stores.get_dtype_counts()

# it gives you count of culumns of non blanks . loc is column name and values are non blank couluns count
df_stores.count()

# It gives blank column count
nrows-df_stores.count()
