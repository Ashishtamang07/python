
class Employee:
    no_employee= 0
    raise_amount= 1.4
    def __init__(self, first_name, last_name, pay):
        self.first_name= first_name
        self.last_name= last_name
        self.pay= pay
        self.email= first_name +"."+ last_name +"@gmail.com"
        Employee.no_employee += 1
    
    
    def fullname(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.pay}"
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
    
    # def __repr__(self):
    #     return f"{self.first_name} {self.last_name} {self.pay} {self.email}"
    
    def __str__(self):
        return f"{self.fullname()} {self.pay} {self.email}"
  
emp1 = Employee("ashish","tamang",100000 )
print(emp1)