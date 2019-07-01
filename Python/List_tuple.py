tup1 = 1,2,3,4,5,6
print(tup1)
type(tup1)

tup2 = (78687,8759684,-4586045,"4645","Basha","Manish","Vimal",34534.10,True,'Basha')
tup2
tup2[2]
tup2[1:5]
tup2[3:]
print(dir(tup1))

list1 = [78687,8759684,-4586045,"4645","Basha","Manish","Vimal",34534.10,True]
len(list1)

# dir gives attributes and functions of perticular object i.e list, touple, srt, int etc.
print(dir(list1))

#Actually copying list
actual_bu = list1.copy()
print(actual_bu)
list1.pop()
print(list1)
