#Duck Typing and Easiser to ask forgiveness then permisssion(EAFP)
class Duck:
    def quack(self):
        print("quack , quack")
        
    def fly(self):
        print("fly , fly")

class Person:
    def quack(self):
        print("iam qucaking like a duck")
        
    def fly(self):
        print("iam flapping my arms ")
        
        
def quack_and_fly(obj):
    # non duck-typed , non-pythonic
    """
    check the object type if obj is duck then run 
    """
    if isinstance(obj, Duck):
        obj.quack()
        obj.fly()
        
    else:
        print("this has to be a duck")
         
d = Duck()
quack_and_fly(d)
d = Person()
quack_and_fly(d)

# output:
# quack , quack
# fly , fly
# this has to be a duck