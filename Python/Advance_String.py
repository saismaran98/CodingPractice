
escapeChar='say hi to bob\'s mom' #\:escape character. 
print(escapeChar)
multilineString="""This is a paragraph
that can recognise \\n characters"""
print(multilineString)
#.isUpper(), isLower(), .lower(), .upper(), .isalnum():is alphanumeric, .isalpha():only alphabatical 
# .isSpace(): check if char is space, .startswith(), .endswith(), 
# join strings combined with this delimeter.ex:
print('# '.join(['name1', 'name2','name2=3'])) #name1# name2# name2=3
#.split()
name='my name is simond'
print(name.split('delemeter_for_split')[0]) #my as it created a list ['my', 'name', 'is', 'simond']
#.rjust(), ljust(),center : add spaces to make length adjusted
print('MyWebsite'.ljust(20,'*'))#MyWebsite***********
print('MyWebsite'.rjust(20,'-'))#-----------MyWebsite
print('MyWebsite'.center(20,'#'))# #####MyWebsite######

#strip white space from left right center
spam='Hello'.rjust(10) #    Hello
spam=spam.strip()#Hello, remove all white space. 
print(spam)
spam='randomNamrandomerandom'
print(spam.strip('random'))#Namrandome removed from lsplit, rsplit i.e left and right

#pyperclip can copy and paste into clipboard. you can use copy and paste. 

#--------String formatting-----------------
#Conversion specifiers. 
name='Alice'
place='main street'
time='6pm'
food='vegan food'
#traditional concatination: poor readability.
invite='Hello '+name+'You are invited to ..'+place+'at'+time+'please bring'+food+'.'
#with Conversion specifiers. (good readable code. )
invite='Hello %s, you are invited to %s at %s please bring %s.'%(name, place, time, food)
print(invite) #Hello Alice, you are invited to main street at 6pm please bring vegan.