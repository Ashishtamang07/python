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
  #LBYL(look before you leave) non pythonic
  """
  if obj have quack method and callable then call it
  """
  if hasattr(obj,'quack'):
    if callable(obj.quack):
      obj.quack()
         
  if hasattr(obj, "fly"):
      if callable(obj.fly):
          obj.fly()
         
d = Duck()
quack_and_fly(d)
d = Person()
quack_and_fly(d)

# output:
# quack , quack
# fly , fly
# iam quacking like a duck
# iam flapping my arms 
