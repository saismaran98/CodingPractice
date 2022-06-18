#Item in dict are on ordered!! similar to Java Map.
import pprint
employeeDB={
    'Key':'Value',
    'employee1':{
    'Name':'Ross',
    'Age': 28},

    'employee2':{
    'Name':'Joey',
    'Age': 30}
}
#Dict Keys
for keys in employeeDB.keys():
    print(keys)
#Dict Values
for values in employeeDB.values():
    print(values)

#Get EMP Details
for employee in employeeDB:
    print(employeeDB.get(employee, 'No element'))

employeeDB.setdefault('Key','default_value') #if Key is missing then it will set the default value if present then Not do anything
print(employeeDB)

String = 'Its a new day and its sunny'
#for character in list(String.lower()):
#    print(f'{character} - {String.lower().count(character)}')
#or
count={}
for character in String.lower():
    count.setdefault(character,0) #needed as first time key will not prsent and interpreter will throw error because of this. 
    count[character]=count[character]+1
print (count)
#pprint=pretty print. 
pprint.pprint(count)