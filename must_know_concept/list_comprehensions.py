"""list comprehensions, its writing loop inside list"""
"run this loop 10 times where i is counter and 0"
x= [ i for i in range(10)]
print(x)
# output-[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x= [ [] for i in range(10)]
print(x)
# output - [[], [], [], [], [], [], [], [], [], []]
x= [ [j for j in range(4)] for i in range(10)]
print(x)
# # output [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]
# "print even number in list form 0 to 9 "
x= [i for i in range(10) if i%2 ==0]
print(x)
# output [0, 2, 4, 6, 8]