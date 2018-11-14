#Dictionaries are Key Value pairs 
#Dictionary will be represented using {flower brackets}

dict ={ 'Height':10, 'Width':20} 
type(dict) 

 
#access elements by key 
print(dict['Height']) 
print(dict['Width']) 

 
#Alternate way to access elements by key 
print(dict.get('Height')) 
print(dict.get('Width')) 

 
#Replace width value 
dict['Width'] = 50 

 
#Access keys 
print(dict.keys()) 

 
#Access both key values pairs 
print(dict.items()) 
