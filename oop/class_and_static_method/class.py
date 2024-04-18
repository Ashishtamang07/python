
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
        return f"{self.first_name} {self.last_name} {self.email}"
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        
    @classmethod
    def from_string(cls, str_emp):
        first_name , last_name , pay = str_emp.split('-')
        "pass it to init"
        return cls(first_name, last_name, pay) 
        
"""usecase: we have first_name last_name and pay in string, seperated by '-'
   so to create instance from it we split string manaully and pass it to constructor
"""
# emp_str1= "jhon-smith-20000"
# emp_str2= "smrit-limbu-10000"
# first_name , last_name , pay = emp_str1.split('-')
# new_emp1= Employee(first_name, last_name,pay)
# print(new_emp1.first_name)

# """same usecase can be done by class method 
# """
# emp_str1= "jhon-smith-20000"
# new_emp1= Employee.from_string(emp_str1)
# print(new_emp1.first_name)


