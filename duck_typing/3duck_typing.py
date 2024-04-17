#Duck Typing and Easiser to ask forgiveness then permisssion(EAFP)
class Duck:
    def quack(self):
        print("quack , quack")
        
    def fly(self):
        print("fly , fly")

class Person:
    def quack(self):
        print("iam quacking like a duck")
        
    def fly(self):
        print("iam flapping my arms ")
  
        
def quack_and_fly(obj):
 #pythonic way , wasier to ask forgivness then permission
 # -insted of asking can we do it ? we try to do it,
 # -if its work great if doesnt work then we catch error and handel it  
 
    try: 
        obj.quack()
        obj.fly()
        obj.bark()
    except AttributeError as e:
        print(e)

 
d = Duck()
quack_and_fly(d)
d = Person()
quack_and_fly(d)

# output:
# quack , quack
# fly , fly
# 'Duck' object has no attribute 'bark'
# iam quacking like a duck
# iam flapping my arms 
# 'Person' object has no attribute 'bark'