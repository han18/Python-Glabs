a = 32         # Initialize the value of a  
b = 6          # Initialize the value of b  
print('a=b:', a==b)  #
print('a+=b:', a+b)  # shorthand of a = a + b
print('a-=b:', a-b)  # shorthand of a = a - b
print('a*=b:', a*b)  # shorthand of a = a * b
print('a%=b:', a%b)  # shorthand of a = a % b
print('a**=b:', a**b)  # shorthand of a = a ** b
print('a//=b:', a//b)  # shorthand of a = a/ b  
   
j = 10 # j gets the value 10.
print("j is : " , j)
j = 5 # j gets the value 5. The previous value is overwritten.
k = j # k gets the value 5.
print("j is : " , j)
print("k is : " , k)


k = j = 10; # (k = (j = 10))
print("j is : " , j)
print("k is : " , k)