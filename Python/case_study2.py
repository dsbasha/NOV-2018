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

#Case Study 5
s=''
for i in range(2000,3201):
    if i%7==0 and i%5==0:
        s=s+str(i)+','
print(s)

#Case Study 6
def area(len, shape):
    area = 0
    if shape.upper() == "CIRCLE":
        area = 3.14*len*len
    if shape.upper() == "SQUARE":
        area = len*len
    return area

print("Area of the Square is: ",area(10,"square"))
print("Area of the Circle is: ",area(10,"circle"))

def area1(*a):
    area = 0
    if a[1].upper() == "CIRCLE":
        area = 3.14*len*len
    if a[1].upper() == "SQUARE":
        area = len*len
    return area 

print("Area of the Square is: ",area(10,"square"))
print("Area of the Circle is: ",area(10,"circle"))
