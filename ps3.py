###### this is the third .py file ###########

#!/bin/python
import ast
dict1 = {'place': 'IIT roorkee', 'city': 'Roorkee', 'state': 'Uttarakhand'} 
dict2 = {'place': 'IIT kanpur', 'city': 'Kanpur', 'state': 'Uttar pradesh'}
dict3 = {'place': 'IIT mumbai', 'city': 'mumbai', 'state': 'maharashtra'}
print dict1
print dict2
print dict3


def add(dict1,dict2,dict3):       #define the function for adding a field in dictionary
	dict1.update({'name': 'mr. ram'})
	dict2.update({'name': 'mr. shyam'})
	dict3.update({'name': 'ms. neha'})
	print dict1
	print dict2
	print dict3
	return

def delete(dict1,dict2,dict3):    #define the function for deleting
	dict1.clear()
	dict2.clear()
	dict3.clear()
	print dict1
	print dict2
	print dict3
	return

def update(dict1,dict2,dict3):     #defining a function for updating
	dict1['city'] = 'meerut'
	dict2['state'] = 'punjab'
	dict3['place'] = 'abcd'
	print dict1
	print dict2
	print dict3
	return
str = input("enter 1 for add, 2 for delete and 3 for update: ")
if str == 1:
	add(dict1,dict2,dict3)
elif str == 2:
	delete(dict1,dict2,dict3)
elif str == 3:
	update(dict1,dict2,dict3)
else:
	var = raw_input("address: ")
	print var


	
