#Assing muiltiple values
'''
many values to multiple variables:
Python allows you to assign values to multiple variables in one line
'''
x,y,z='apple','banana','orange'
print(x)
print(y)
print(z)

#assing one value to multiple varibales
'''
you can assign the same value to multiple variables in one line
eg:
'''
a = b = c = "apple"
print(a)
print(b)
print(c)

#unpacking a collection
'''
If you have a collection of values in a list, tuple etc. 
Python allows you to extract the values into variables. This is called unpacking.
'''
fruits=['apple','organe','banana']
e,f,g=fruits
print(e)
print(f)
print(g)

#python -output variables
'''
output variables
The Python print() function is often used to output variables.
'''
j='food is awesome'
print(j)

#In the print() function, you output multiple variables, separated by a comma
l='the '
v='dog '
w='is playing'
print(l,v,w)

#You can also use the + operator to output multiple variables
print(l + v + w)

'''
Notice the space character after "Python " and "is ", without them the result would be "thedogis playing".
For numbers, the + character works as a mathematical operator
'''
i=5
o=10
print(i+o) #15

#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error

'''
just like this
x = 5
y = "John"
print(x + y)
'''

'''
The best way to output multiple variables in the print() function is to separate them with commas,
which even support different data types:
'''
x = 5
y = "John"
print(x , y)

#Global Variables
'''
Variables that are created outside of a function  are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.
'''
h='beautiful'

def myfun():
    print('girl is ' + h)
    
myfun()

'''
If you create a variable with the same name inside a function, 
this variable will be local, and can only be used inside the function. 
The global variable with the same name will remain as it was,
global and with the original value. 
'''
k='playing'
def myfunc():
    k="sleeping"
    print('dog is '  + k)
myfunc()
print('dog is ' + k)

#global keyword
'''
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
To create a global variable inside a function, you can use the global keyword.
'''
q="xuv"
def mycar():
    global q
    q ='BMW'
mycar()
print('i have a car ' + q)    

#Also, use the global keyword if you want to change a global variable inside a function.