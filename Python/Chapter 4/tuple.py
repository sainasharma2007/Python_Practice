a=(1,2,3,4,5)
print(type(a))

# empty tuple
b=()
print(b)

# tuple is immutable
# c=(56,987,23,"Saina",False,45.87)
# c[2]=65
# print(c)

# concatenation
A=(23,45,67)
B=(12,45,89)
con=A+B
print(con)

# repetition 
A=(23,45,67)
rep=A*4
print(rep)

# membership
A=(23,45,67)
print(100 in A)

# length 
A=(23,45,67)
print(len(A))

# slicing 
A=(23,45,67)
print(A[:2])

# min and max
A=(23,45,67)
print(min(A))
print(max(A))

# unpacking
A=(23,45,67)
x,y,z=A
print(x,y,z)