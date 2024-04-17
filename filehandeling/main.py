# context manager, we have access to f out of context manager as well
with open("file.txt", 'r') as f:
    
    f_content= f.read(100)
#     print(f_content,end='')
    
with open("file2.txt", 'w') as f:
    "seek(0) override 1st line by 2nd line from index3 of hello ashish "
    f.write("hello ashish")
    f.seek(3)
    f.write("ashish ")

"""
from original file file.text read and write to new file file_copy.txt
"""
with open("file.txt", 'r') as of:
    with open("file_copy.txt" ,'w') as cf:
        
        for line in of :
            cf.write(line)
"""
working with images
"""
with open ("dog.png", 'rb') as of:
    with open("dog_copy.jpg" , 'wb') as cf:
        for line in of :
            cf.write(line)