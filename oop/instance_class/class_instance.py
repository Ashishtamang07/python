class Employee:
    def __init__(self, first_name, last_name):
        self.first_name= first_name
        self.last_name= last_name
        self.email= first_name + last_name +"@gmail.com"
    

    
emp2= Employee(first_name="sabina", last_name="tmanag")
print(emp2.email)
print("{} {} {}".format(emp2.first_name, emp2.last_name , emp2.email))
print(f"{emp2.first_name} {emp2.last_name} {emp2.email}")

"manaully setting obj attr"
# emp1= Employee()
# emp1.first_name="ashish"
# emp1.last_name="tamang"
# emp1.email= "ashishtmanag@gmail.com"
# print(emp1.email)