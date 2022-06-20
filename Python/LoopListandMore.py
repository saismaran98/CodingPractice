#collection of integer 
from re import A


val=list(range(2,20)) #returns list of integer 2 to 20 (initial value, final value(not included), step)
for value in range(2,5,2):
    print(value)
print(val)
#Python multiple assignment 
listOne=[1,2,3]
int1, int2,int3=listOne
#or
int4, int5, int6=4,5,6
print(int1, int5) #prints 1 5
#--Use Case 1: to swap variables
a='value1'
b='value2'
a, b = b, a
print(a, b) #value2 value1

#augmented assignment operator
#a=a+'value3' insted we can use
a+='value3'
print(a)

