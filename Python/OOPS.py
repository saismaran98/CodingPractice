 #object-oriented programming in python

from calendar import weekday
from datetime import datetime



class Employee:
    no_of_employee=0
    companyName="Global"
    day="Sunday"
    def __init__(self, first, last, pay):  #python constructor (this, parm1,...)
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@'+self.companyName+'.com'
        Employee.no_of_employee+=1
    
    def toString(self):
        return f'Hi {self.first}, your company email id is {self.email}, {self.companyName}'
    #Class Method: Insted of modifying variable with respect to instance we modify 
    # with respect to class which then will be comon for all instances. 
    @classmethod
    def changeCompanyName(cls, newName):
        cls.companyName=newName
    @staticmethod
    def isWorkDay(day):
        print(day)
        if day.weekday()==5 or day.weekday() == 6:
            return False
        return True
def main():
    Ross=Employee("Ross","Geller",400000)
    Chandler=Employee("Chandler","Bing",800000)
    print(Ross.toString()) #or Employee.toString(Ross)
    print(f'total emp count{Employee.no_of_employee}, company-name: {Chandler.companyName}')
    Ross.companyName='Global-New' #change only instance company value, Employee.companyName change for class level
    print(Ross.toString())          
    print(Chandler.toString())
    import datetime
    my_date = datetime.date(2021, 3, 2)
    print(Employee.isWorkDay(my_date))
    #print(Employee.__dict__) # __dict__ returns the dictionary used to implement the module’s namespace
if __name__=="__main__":
    main()