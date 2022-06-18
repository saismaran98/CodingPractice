def functionOne():
    print("Inside Function One")
def functionTwo(name):
    print("Hello "+name);
#    for ch in name:
#        print(ch)

#to visualise and see execution see pythontutor
#Calling Methods
functionOne()
functionTwo("UserName")    # Output: Hello UserName

#if a function does not have a return value its default is None ex, 
varOne=print() #waht is return for print method with no parameter, its none
#to verify we can print 
print(None==varOne) #prints True 

#Keyword Arguments are optional argument. ex. end for print
print('same', end='')
print('line') #sameline
