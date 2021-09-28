
#diferint ways to convert a string into a list

#this takes user input
x = input("put a word in here ")
print(x)    #and returns a string
c = list(x)    #this turns it into a list
print(c)    #and prints it out as a list
v = [char for char in x]    #this dose the same thing but uses a loop
print(v)    #and prints it out as a list
b = list(x[0:])    #this turns it into a list and prints out every char starting from 1st pos
print(b)    #and prints it out as a list
n = "".join(b)    #and this takes a list and turns it into a string
print(n)    #and prints it out as a list