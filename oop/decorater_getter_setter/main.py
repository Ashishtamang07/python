
class Employee:
    no_employee= 0
    raise_amount= 1.4
    def __init__(self, first_name, last_name):
        self.first_name= first_name
        self.last_name= last_name
        Employee.no_employee += 1
    "decorator can be access like an attribute"
    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@gmail.com"
    "getter"
    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    "setter"
    @fullname.setter
    def fullname(self, name):
        first, last= name.split(" ")
        self.first_name= first
        self.last_name= last
        
    @fullname.deleter
    def fullname(self):
        print("delete name")
        self.first_name= None
        self.last_name= None
    
emp1= Employee("ashish", "tamnag")
emp1.fullname= 'rubina shrestha'


print(emp1.first_name)
print(emp1.email)
print(emp1.fullname)
del emp1.fullname
