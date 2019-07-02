def sqrt(x):
    res = x**(1/2)
    return res
print(sqrt(25))

def power(x,p=1):
    res = x**p
    return res
print(power(5,2))
print(power(5))

def add(x=1,y=1):
    return x+y

add(1,3)

def demo1(*x):
    print(x)
    print("Data type of x",type(x))

demo1(2,45,6,456,"dfgdg")

def adv_sum(*x):
    total = 0
    for i in x:
        total += i
    return total

print(adv_sum(2,3,4,5,6))

def demo2(**x):
    print(x)
    print("Data Type of X", type(x))

demo2(Engl=98,Math=99,avg1=67,Venue="England",Y=10)

def funct1(*x,a):
    print(type(x))
    print(type(a))

funct1(2,3,45,6,a=1)
