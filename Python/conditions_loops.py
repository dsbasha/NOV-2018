x=-1

if x>0:
    print("Pos")
else:
    if(x<0):
        print("Neg") 
    else:
        print("Zero")

print("done")

#Using elif
x=0
if x>0:
    print("Pos")
elif x<0:
    print("Neg")
else:
    print("zero")  
 
 
 # Using While loop
n=1
while(n<=10):
    print(n*2)
    n+=1
    
#Using For loop general method
for i in range(0,len(tup1)):
    print(i*10)

for i in tup1:
    if i<20:
     print(i)
