# [list items] this maintain orders. 
from ctypes import sizeof


listCompany=['Adobe', 'IBM', 'Google', 'Microsoft', 'Oracle', 'apple']
listOne=[['string','string2'],[1,2,3,4,5,-1]]
print('ListOne:: {listOne[0]}')
#in and not in
print('string' in listOne[0])       #True as listOne[0] is a list ['string', 'string2'] which has string. 
print('string' not in listOne[0])   #False as listOne[0] is a list ['string', 'string2'] which has string. 
listTwo=[1,2,3,4,5]
print(listTwo[1:4])                 #print elemnt 1 to 3 except 4th element [2, 3, 4]
del listTwo[1]                      #delete element 2 from the list [1, 3, 4, 5]
print(listTwo) 


#-----------ListMethods--------------------
#.index()
print('index of passed int is',listTwo.index(5))
#insert()
listTwo.insert(len(listTwo),6) #element inserted at the end of the list. 
#.append() add element to the end of the list
listTwo.append(3)
#.remove(specific_value_in_list)
listTwo.remove(3)
#.sort() uses ASCII based sorting
intList=[4,5,2,1,56]
asciiList=['Alice', 'Bob','alice', 'bob']
intList.sort()
asciiList.sort()
print(intList, '   ', asciiList)
#to truely sort list of string without worrying about case we can say
asciiList.sort(key=str.lower)
print(asciiList)
#[1, 2, 4, 5, 56]     ['Alice', 'Bob', 'alice', 'bob']
#['Alice', 'alice', 'Bob', 'bob']
#string are immutable in python. 
#we pass list ref to variable when we assign it to a variable. 


listOfBoys = ['Ram','Shyam','Gurprit']
listOfBoys.append('Teddy')
print(listOfBoys)

l1 = [1,[1,2,1,3],3]  #list Under a list
#counts and returns the number of times the specified element obj appears in the list
print(f'count() :: {l1[1].count(1)}') #1 is present twice in list l1[1]: [1,2,1,3]

tup = ('Saismaran',245.0)

#Tuple doesnot allow assign i.e it is immutable i.e maintains data integrity
print(l1.index(3))
print(tup)

#Tuple = () List = []

#   List comprehension:

#   Usual method:


