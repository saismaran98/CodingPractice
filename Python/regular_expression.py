#!pyton3
#import regular expression
import re
#------------Verbose Mode-------------
email='Call me 415-555-101 or 415-111-3444 from 9AM to 6PM'
#Verbose Regular expression:: more readability 
#verbose enable us to use ''' and we can make reg expression more readable
#----------------------------------------------
#to avoid escape caracter \ ex. compile('(\\d\\d\\d') .. we can use r i.e use raw string and directly pass string ('(\d\d\d)')
getNumbers=re.compile(r'''
(\d\d\d)    #area code group()
-           #contains dash 1
\d\d\d      #number digits
-           #contains dash 2
\d\d\d\d    #last 4 digits
''', re.IGNORECASE|re.DOTALL| re.VERBOSE)
print(getNumbers.search(email).group())
#---------------------------------------------
email='Call me 415-555-101 or 415-111-344 from 9AM to 6PM'
#.compile() this compiles the regular expression pattern, r is raw string. 
phoneNumber=re.compile(r'\d\d\d-\d\d\d-\d\d\d')
getNum=phoneNumber.search(email) 

#with iterator. 
getItr=phoneNumber.finditer(email)
print(f'Num01: {getItr.__next__().group()}') #gets all number in the email one by one. 
print(f'Num02: {getItr.__next__().group()}')
#.findall()
#returns list of all match gNu=phoneNumber.findall(email)

#-----------------Regex, groups and pipe------------------------------------------------
email2='Call me 415-555-101 or 415-111-344 from 9AM to 6PM'
#.compile() this compiles the regular expression pattern, r is raw string. 
phoneNumber=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d)')
getNum=phoneNumber.search(email2) 

#with iterator. 
getItr=phoneNumber.finditer(email2)
print(f'AreaCode: {getItr.__next__().group(1)}') #AreaCode: 415
print(f'Number: {getItr.__next__().group(2)}')#Number: 111-344

fileContent='Batwoman\'s batmobile is very fast.'
#pipe (|)
regex=re.compile(r'bat(mobile|man|copter)')
ifContains=regex.search(fileContent)
print(ifContains.group())
#?
regex=re.compile(r'Bat(wo)?man') #equivalent to (Batman|Batwoman) i.e wo can occor 0 or more time
ifContains=regex.search(fileContent)
print(ifContains.group()) #seaches both batman and batwoman

phoneNumber=re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d')
getNum=phoneNumber.search('my num without area code 444-555-245') 
print(getNum.group())

countRegex=re.compile(r'(Ha){3}')   #(ha){3} consequtively 3 times. 
print(countRegex.search('He laughed HaHaHa').group()) 

digitRegex=re.compile(r'(\d){3,5}') # {min_num, max_num times} #greedy Match
digitRegex=re.compile(r'(\d){3,5}?') # {min_num, max_num times} #non-greedy Match
print(digitRegex.search('12345679')) #greedy Match: as 5 is max_num it will print first 5 digit.1,2,3,4,5 i.e longest possible string
print(digitRegex.search('12345679')) #non-greedy Match: as 3 is min_num it will print first 3 digit. 1,2,3 


#Findall()
contact='email: email@domain.com, ph: +91-8899098978, linkedin=https://www.linkedin.com/user-name'
getMobNo_regex=re.compile(r'(\+\d\d)?-(\d\d\d\d\d\d\d\d\d\d)')
print('getMobNo_regex: ', getMobNo_regex.findall(contact)) #returns a list of touple of areaCode and number getMobNo_regex:  [('+91', '8899098978')]

#Characted Class \d, \D, \w, \W, \s, \S see below for defination.
vowelRegex=re.compile(r'[A-Za-z]*[aeiouAEIOU][a-z]*') #or (r'[A-Za-z]*[aeiou][a-z]*', re.IGNORECASSE) i,e ignoring case
vowelRegex=re.compile(r'[A-Za-z]*[aeiouAEIOU]{2}') #two consequetive vowels
consonantRegex=re.compile(r'[^aeiouAEIOU]?') #i.e ^ not aeiouAEIOU
print(vowelRegex.findall('This is the string to check vowel nn ttllpp'))
#print(consonantRegex.findall('This is the string to check vowel nn ttllpp'))

beginsWithHello=re.compile(r'^Hello')#beginsWith
print(beginsWithHello.search('Hello This string does not start with hello'))
endsWithRegex=re.compile(r'world$') #if word ends with 
print(endsWithRegex.search('Hello world'))
allDigitsRegex=re.compile(r'^\d+$') #^beings with \d(digit)+(one-or more) $(ends with digit.)
print(allDigitsRegex.search('435466435')) #yes all digit and return digit value
print(allDigitsRegex.search('435466fg435'))#not all digit returns None

#wildcard character. *
atRegex=re.compile(r'.at') # . single character followed by at 
print(atRegex.findall('mat bat can flat mindat'))#['mat', 'bat', 'lat', 'dat'], flat is double char preceeding at. 
# .* =anything , operates in a greeedy match
dotStarRegex=re.compile(r'First Name: (.*) Last Name: (.*)')
print(dotStarRegex.findall('First Name: David Last Name: Malan'))#[('David', 'Malan')]

string01='<To Serve Chicken> for Dinner>'
nongreedyRegex=re.compile(r'<(.*)>')
#? for non-greedy. 
print(nongreedyRegex.findall(string01))#['To Serve Chicken'], without ? in (.*) we get greedy match ['To Serve Chicken> for Dinner']
#. matches any char except \n i.e next line, to make it accept new lines we can pass '.*', re.DOALL

#Protect Confidencial Data
namesRegex=re.compile(r'Agent \w+',re.IGNORECASE) #Agent followed by the word i.e agent name. 
#print(namesRegex.findall('This is Agent Bob reporting with agent Alice.')), found all agent names, now we can redact using sub command
print(namesRegex.sub('REDACTED','This is Agent Bob reporting with agent Alice.')) #substitute agent names found in findall with 'REDACTED'

newNameRegex=re.compile(r'Agent (\w)\W*')
#(\w) one word in the group 
print(newNameRegex.sub(r'Agent \1**** ','Agent Alice give files to Agent Bob')) #\1 is first word of the group found in findall() ex. Alice \1=A







#---------------------Notes----------------------------------------------
# group():   Return the string matched by the RE
# start():   Return the starting position of the match
# end():     Return the ending position of the match
# span():    Return a tuple containing the (start, end) positions of the match

# match():   Determine if the RE matches at the beginning of the string.
# search():  Scan through a string, looking for any location where this RE matches.
# findall(): Find all substrings where the RE matches, and returns them as a list.
# finditer():Find all substrings where the RE matches, and returns them as an iterator

#\d:  Matches any decimal digit; this is equivalent to the class [0-9].
# \D: Matches any non-digit character; this is equivalent to the class [^0-9].
# \s: Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v].
# \S: Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].
# \w: Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_].
# \W: Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].
# These sequences can be included inside a character class. For example, [\s,.] is a character class that will match any whitespace character, or ',' or '.'."""
