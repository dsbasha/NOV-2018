# Case study 1
x = input("Enter the number: ")
print(x)

if int(x)>0:
    print(x+ " is Positive")
elif int(x)<0:
    print(x+ " is Negative")
else:
    print("Zero") 
    
# Case study 2
 x = input("Enter the number: ")
print(x)

if int(x)%2 == 0:
    print(x+ " is Even Number")
else:
    print(x+ " is Odd Number")
    
 # Case study 3
x = input("Enter the Year: ")

while (len(x) <4):
    x = input("Enter the valid the Year: ") 

if int(x)%400 ==0:
    print (x+ "is a leap year")
else:
    print (x+ "is a not a leap year")
    
# Case study 5
a = input("Enter the First Number: ")
b = input("Enter the Second Number: ")
c = input("Enter the Third Number: ")

if(a>b and a>c):
    print ("Largest number is "+a)
elif(b>a and b>c):
    print ("Largest number is "+b)
else:
    print ("Largest number is "+c)
   
# Case study 5
month = input("Enter the Month Name: ")

if (month.upper() == "JAN") or (month.upper() == "JANUARY"):
    print ("January contains 31 Days")
elif(month.upper() == "FEB") or (month.upper() == "FEBRUARY"):
    print ("February contains 28/29 Days")
elif(month.upper() == "MAR") or (month.upper() == "MARCH"):
    print ("March contains 31 Days")
elif(month.upper() == "APR") or (month.upper() == "APRIL"):
    print ("Apri contains 30 Days")
elif(month.upper() == "MAY"):
    print ("May contains 31 Days")
elif(month.upper() == "JUN") or (month.upper() == "JUNE"):
    print ("June contains 30 Days")   
elif(month.upper() == "JUL") or (month.upper() == "JULY"):
    print ("July contains 31 Days"
    
#Alternative
months = ['Jan',31,'Feb','28/29','Mar',31,'Apr',30]
month = input("Enter the Month Name MMM: ")
print(month+ " Contains " +str(months[months.index(month)+1])+" Days")

# Case study 6
a = input("Enter the any Number: ")
num = int(a)
isPrime = True
for i in range(2,num):
    if num%i == 0:
        isPrime = False
if isPrime:
    print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")

#Print Primes from Range
primelist =[]
for posibleprime in range(2,22):
    isPrime = True
    for num in range(2,posibleprime):
        if posibleprime%num == 0:
            isPrime = False
    if isPrime:
        primelist.append(posibleprime)
print(primelist)
           
#Case Study 7
n=int(input("Enter number:"))
fact=1
while(n>0):
    fact=fact*n
    n=n-1
print("Factorial of the number is: ")
print(fact)

#Case Study 8
num = int(input("Enter the number to show multiplication table of"))  
# using for loop to iterate multiplication 10 times   
for i in range(1,11):  
   print(num,'x',i,'=',num*i) 

#Case Study 9
fibonacci = int(input("Enter the number for Fibonacci Sequence "))  

if fibonacci <= 0:  
    fibonacci = int(input("Please Enter the Positive number "))

n1 = 0  
n2 = 1  
count = 2

if fibonacci == 1:  
   print("Fibonacci sequence:")  
   print(n1) 
    
else:  
    print("Fibonacci sequence:")  
    print(n1)
    print(n2)  
    while count < fibonacci:  
        nxt = n1 + n2  
        print(nxt)  
       # update values  
        n1 = n2  
        n2 = nxt  
        count += 1
           
 #Case Study 10
num = int(input("Enter the number: "))
temp = num
tot = 0
if num <= 0: 
    print("Enter a whole positive number!") 
else: 
    while num > 0:
        tot = tot + num
        num = num - 1;
    # displaying output
    print("Sum of first", temp, "natural numbers is: ", tot)
