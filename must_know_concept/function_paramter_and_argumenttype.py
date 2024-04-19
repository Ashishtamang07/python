def complicated_function(x,y):
    print(x, y)
    
complicated_function(1,3) # positional args
# complicated_function(x=1,y=3) # keyword args
"""postional args cant follow keyword args,
meaning 1st args should be positional 
"""
def complicated_function(x,y):
    print(x, y)
    
complicated_function(1,y=3) # ok 200
# complicated_function(x=1,3) # error
# output SyntaxError: positional argument follows keyword argument
"optional parameter"
def complicated_function(x,y, z=None):
    print(x, y)
    
complicated_function(1,3) # ok 200

