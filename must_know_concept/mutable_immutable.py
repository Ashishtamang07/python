"x cant modify coz its immubale"
# x=(1,2)
# x[0] =4
"""working with immutable, [modifiaction doesnt allowed],
when we do assigment to new vairable
like y=x, its make copy of object to its memory address,
same same object but its diffent.  

"""
# x=(1,2)
# y=x
# x=(1,2,3,4) #"reassigning to x to new obj (1,2,3,4)"
# print(x,y)
# output
# (1, 2, 3, 4) (1, 2)
""" working with mutable,
here we expect [100,2] [1,2] y dont change, but it changes to [100,2] [100,2]
because x and y store the refrence of the same object in memory
making assigmnet obj to new variable, both vairable point to same object ,
so if we modify x obj, y obj will be modify
"""
# x=[1,2]
# y=x
# x[0]=100
# print(x,y)

def get_largest_number(numbers, n):
    numbers.sort()
    return numbers[-n]
nums= [2,3,1,5,8,6]
print(nums)
get_largest_number(nums, 2)
print(nums)