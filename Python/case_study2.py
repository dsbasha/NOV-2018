# Case Study 1
val=int(input("Enter The number:"))

if val%2==0:
    print(val," Is a Even Number")
else:
    print(val," Is a Odd Number")
    
# Case Study 2
def largest(a,b,c):
    largest = 0
    if(a>b and a>c):
        largest = a     
    elif(b>a and b>c):
        largest = b  
    else:
        largest = c
    return largest

largest(5,17,45)

# Case Study 3
def mult_table(x):
    for i in range(1,11):  
        print(num,'x',i,'=',num*i) 
    
num = int(input("Enter the number to show multiplication table of"))  
mult_table(num)

