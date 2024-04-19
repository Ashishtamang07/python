# """
# *args, accept any no. of positional agrs even NO args and store in tuple
# """
# def complicated_function(*agrs):
#     print(agrs)
# # complicated_function(1,3,2,3,4,)#output (1, 3, 2, 3, 4)
# complicated_function()#output ()

# "*kwargs, accept any no. of keyword args even NO args and store in dictionary "
# def complicated_function(*args,**kwargs):
#     print(args, kwargs)
# complicated_function(x=1,s=2,m="ashish")#output () {'x': 1, 's': 2, 'm': 'ashish'}
# # complicated_function()#output () {'x': 1, 's': 2, 'm': 'ashish'}
# """
# list unpacking , *[1,2] this will break a list into two positional args and pass like (1,2)
# dictionary unpacking, **{"c"="hello","s":"tamang"} this will break a dictionary into two keyword args and pass like (c="hello",s="tamang")
# """
def complicated_function(a,b,c=None , d=False):
    print(a,b,c,d)
complicated_function(*[2,7], **{"c":"hello","d":"tamang"}) #list unpacking and dictionary unpacking
