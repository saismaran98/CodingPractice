from ast import Try

#without try and catch program execution will stop after this line as python is a interpreter language so its important to handle exceptions
#we can also do input validation with try except. 
def div(num1, num2):
    return num1/num2

def betterDiv(num1, num2):
    try:
        return num1[0]/num2
    except ZeroDivisionError:
        return 'Error, You paassed num2 as 0'
    except:
        return 'Unknown Error, i.e Generic error handled by except.'

#-------MethodCalls----------#
print(div(1,2))
print(betterDiv(1,0)) 
print(div(2,3))

#-------InputValidation----------#
#def expects int value to perform logic
def passOrFail(score):
    try:
        if score > 80 and score < 100:
            print('You passed azure-900')
        elif score <80 and score >0:
            print('You did not pass')
        else:
            print('Error: Value is out of range!')
    except TypeError:                    #input validation
            print('Input is not a number')
    except:
        print('Generic Exception')

passOrFail(100.2)