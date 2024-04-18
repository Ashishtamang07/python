
class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name= first_name
        self.last_name= last_name
        self.pay= pay
        self.email= first_name +"."+ last_name +"@gmail.com"
        Employee.no_employee += 1
    
    
    def fullname(self):
        return f"{self.first_name} {self.last_name} {self.email}"
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
import datetime
my_date= datetime.date(2024, 7, 10)
print(Employee.is_workday(my_date))
        


