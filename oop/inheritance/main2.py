"""
we have manager class that manages employee
"""
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
"dont pass mutable datatype like list, dict as default agrs , so employee:None"

class Manager(Employee):
    def __init__(self, first_name, last_name,pay, employee:None):
        super().__init__(first_name, last_name, pay)
        if employee is None:
            self.employee = []
        else:
            self.employee = employee
            
    def add_emp(self, emp):
        " if emp instance is not in self.employee add"
        if emp not in self.employee:
          self.employee.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employee:
            self.employee.remove(emp)
    def print_emp(self):
        for emp in self.employee:
            print("-->", emp.fullname())
 
emp1= Employee("rubina","shrestha", 10000)       
emp2= Employee("sabina","khadka", 88800)       
manager1=Manager("ram" , "tamanag", 30000, [])
# print(manager1.email)
# manager1.print_emp()
# manager1.add_emp(emp1)
# manager1.add_emp(emp2)
# manager1.print_emp()
# output
# --> rubina shrestha rubina.shrestha@gmail.com 10000
# --> sabina khadka sabina.khadka@gmail.com 88800
print(isinstance(manager1, Employee))  #true 
print(issubclass(Manager, Employee))   #true