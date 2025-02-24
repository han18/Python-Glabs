
a = 5          # initialize the value of a    
print('Is this statement true?:',a > 3 and a < 5)  
print('Any one statement is true?:',a > 3 or a < 5)  
print('Each statement is true then return False and vice-versa:',(not(a > 3 and a < 5)))

# Example: Identity Operators

a = ["Rose", "Lotus"]
b = ["Rose", "Lotus"]
c = a
print(a is c)
print(a is not c)
print(a is b)
print(a is not b)
print(a == b)
print(a != b)


# 
x = ["Rose", "Lotus"]  
print(' Is value Present?', "Rose" in x)  
print(' Is value not Present?', "Riya" not in x)    


x = 'Hello world'
y = {1:'a', 2:'b'}


# check if 'H' is present in x string
print('H' in x)  # prints True
# check if 'hello' is present in x string
print('hello' not in x)  # prints True
# check if '1' key is present in y
print(1 in y)  # prints True
# check if 'a' key is present in y
print('a' in y)  # prints False


