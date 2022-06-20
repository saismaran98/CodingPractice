from msilib.schema import Property
import OOPS

class Developer(OOPS.Employee):
    def __init__(self, first, last, pay,progLanguage):
        super().__init__(first, last, pay)
        self.progLanguage=progLanguage

class FullStackDeveloper(Developer):
    def __init__(self, first, last, pay, progLanguage,skill=None):
        super().__init__(first, last, pay, progLanguage)
        self.skill=skill
    @property
    def getSkills(self):
        return self.skill
    @getSkills.setter   #as getSkills is a property we can have a setter for that. 
    def skillsadd(self, newSkill):
        self.skill.append(newSkill)
    def __str__(self) -> str:
        return super().__str__()
dev01=Developer('Lewis', 'Hamilton',200000, 'Driver')
fsd01=FullStackDeveloper('Max','Verstappen', 200000,'Java',['Mongo','Reach','Azure'])
#print(fsd01) #becasuse of __str__ i get a proper object print ('Max', 'Verstappen', 200000, 'Java', ['Mongo', 'Reach', 'Azure'])
#print(fsd01.getSkills) #['Mongo', 'Reach', 'Azure']
fsd01.skillsadd='Python' #added method python 
print(fsd01.skill)