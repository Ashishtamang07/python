" developer and manager are sub class to employee"
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
"developer has extra attr ie salary so,"       
class Developer(Employee):
    def __init__(self, firs_name , last_name, pay , prog_lang):
        super().__init__(firs_name,last_name, pay)
        # Employee.__init__(self, firs_name , last_name ,pay)
        self.prog_lang= prog_lang
  
# print(help(type(Developer)))

dev1= Developer("ashish","rubina",2000,"python")
dev2= Developer("sabina","tamang",40000,"java")
# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)
# print(dev1.__dict__)
print(dev1.email)
print(dev2.prog_lang)

