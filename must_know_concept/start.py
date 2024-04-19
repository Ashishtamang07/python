"""
if the file is run as main scripts then it will run the code
if the file is imported then it will not run the code only export the code
if there is no if __name__=="__main__": and import the file ,
and try to run its functionalities then it will run twice
"""
def add(a, b):
    return a+b

if __name__=="__main__":
    print(add(2,3))
    print("run")