
class Employee:
    def __init__(self, first_name, last_name):
        self.first_name= first_name
        self.last_name= last_name
        self.email= first_name + last_name +"@gmail.com"
    
    def fullname(self):
        return f"{self.first_name} {self.last_name} {self.email}"
    
emp3= Employee(first_name="rubina" , last_name="tamang")
"by object: instance get pass automatically so we dont pass instance  "
print(emp3.fullname())
"by class: it doesnt know what to run that method with so we pass instance"
print(Employee.fullname(emp3))
    
# TypeError: Employee.fullname() takes 0 positional arguments but 1 was given
#coze in methods instance is pass automatically so we take it as self