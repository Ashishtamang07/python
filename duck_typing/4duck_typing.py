#Duck Typing and Easiser to ask forgiveness then permisssion(EAFP)
person = {"name":"ashish tamang", "age":24, "job":"programmer"}
# person = {"name":"ashish tamang", "age":24}

#LBYL non pythonic way
if "name" in person and "age" in person and "job" in person:
    print("i am {name} and my age is {age} and i work as {job}".format(**person))
else:
    print("missing some keys")
    
# EAFP(pythonic)
try:
     print("i am {name} and my age is {age} and i work as {job}".format(**person))
except KeyError as e:
    print("missing some keys")


my_list=[1,2,3,4,5,6,7]
# non pythonic way
if len(my_list) > 6:
    print(my_list[5])
else:
    print("index does not exist")
    
try:
    print(my_list[7])
except IndexError as e:
    print("index does not exist")