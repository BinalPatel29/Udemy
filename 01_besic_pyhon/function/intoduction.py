#fun is a block of code
#reusimg code
#syntax
def fun_name(parameters):
    """Docstring"""
    #fun body
    return expression

# why fun?
num=24
if num%2==0:
    print("num is even")
else:
    print("num is odd")

def even_or_odd(num):
    if num%2==0:
        print("num is even")
    else:
        print("num is odd")
##call the fun
even_or_odd(24)

##fun with multiple parameters
def add(a,b):
    return a+b
result=add(2,4)
print(result)

# Default parameters
def greet(name):
    print(f"Hello {name} welcome to paradise")
greet("Binal")

def greet(name="Guest"):             ##  by defualt parameter give "Guest"
    print(f"Hello {name} welcome to paradise")
greet()

# Variable length arguments
##Positional and keyword arguments

def print_numbers(*Binal):    #*args
    for number in Binal:
        print(number) 
print_numbers(1,2,3,4,5,6,7,8,"Binal")

### Positional arguments
def print_numbers(*args):    
    for number in args:
        print(number) 
print_numbers(1,2,3,4,5,6,7,8,"Binal")

### Keywords arguments
def print_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_details(name="Binal",age="22",country="india")    

def print_details(*args,**kwargs):
    for val in args:
        print(f"{val}")
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_details(1,2,3,,4,"Binal",name="Binal",age="22",country="india")

#Return statements
def multiply(a,b):
    return a*b
multiply(2,3)

##return multiple parameters
def multiply(a,b):
    return a*b,a
multiply(2,3)