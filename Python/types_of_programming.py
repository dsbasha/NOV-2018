#Traditional functional programming 
TFP = [10,20,30,40,50] 
i = 0 #Initialize 
for x in TFP: 
TFP[i] = x + 10 
i = i + 1 #Increment 
print(TFP) 

 
#Convert above traditional functional programming to better in python 
age = [1,2,3,4,] 
#i = 0 
#Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. 
for i,e in enumerate(age): 
age[i] = e + 10 
print(age) 

 
#Convert above traditional functional programming to MOST EFFICIENT in python by using 
#map is more effective, scalable and parallel process mechanism 
#Use map object instead of for loop 
age = [1,2,3,4,] 
weight = [5,10,15] 
