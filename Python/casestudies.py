# 1st case study
x = input("Enter the number: ")
print(x)

if int(x)>0:
    print(x+ " is Positive")
elif int(x)<0:
    print(x+ " is Negative")
else:
    print("Zero") 
    
#2 case study
 x = input("Enter the number: ")
print(x)

if int(x)%2 == 0:
    print(x+ " is Even Number")
else:
    print(x+ " is Odd Number")
    
 #3 case study
x = input("Enter the Year: ")

while (len(x) <4):
    x = input("Enter the valid the Year: ") 

if int(x)%400 ==0:
    print (x+ "is a leap year")
else:
    print (x+ "is a not a leap year")
    
# 4th Case study
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
if num > 2:  
    for i in range(2,num):  
        if (num % i) == 0:  
            print(num,"is not a prime number")  
            print(i,"times",num//i,"is",num)  
            break  
        else:  
            print(num,"is a prime number")      
else:  
    print(num,"is a prime number")  
