"""class variabel is global vairable ,
-> while accessing class vairable in methods we can access by instance or class vaiable ,
=> class vaiable is shared by all instance ,
when we try to access attrs on in instance , it will check in instance first , if not found then it will check in class ,
if not found then it will check in parent class ,

"""
class Employee:
    no_employee= 0
    raise_amount= 1.4
    def __init__(self, first_name, last_name, pay):
        self.first_name= first_name
        self.last_name= last_name
        self.pay= pay
        self.email= first_name +"."+ last_name +"@gmail.com"
        "increment no. employee every time by 1 if instance is created "
        Employee.no_employee += 1
    
    
    def fullname(self):
        return f"{self.first_name} {self.last_name} {self.email}"
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        
emp1= Employee(first_name="ashish", last_name="tamang", pay= 10000)
emp2= Employee(first_name="sabina", last_name="tamang", pay= 50000)
# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)
# emp1.raise_amount = 2.0
# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)
# print(emp1.__dict__)
print(Employee.no_employee)