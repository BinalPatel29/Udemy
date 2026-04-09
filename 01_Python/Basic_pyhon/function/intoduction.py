#fun is a block of code
#reusimg code
#syntax
# def fun_name(parameters):
#     """Docstring"""
#     #fun body
#     return expression

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
# even_or_odd(24)

##fun with multiple parameters
def add(a,b):
    return a+b
result=add(2,4)
# print(result)

# Default parameters
def greet(name):
    print(f"Hello {name} welcome to paradise")
# greet("Binal")

def greet(name="Guest"):             ##  by defualt parameter give "Guest"
    print(f"Hello {name} welcome to paradise")
# greet()

# Variable length arguments
##Positional and keyword arguments

def print_numbers(*Binal):    #*args
    for number in Binal:
        print(number) 
# print_numbers(1,3,4,7,5,"Binal")

### Positional arguments
def print_numbers(*args):    
    for number in args:
        print(number) 
# print_numbers(1,2,3,4,5,6,7,8,"Binal")

### Keywords arguments
def print_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
# print_details(name="Binal",age="22",country="india")    

def print_details(*args,**kwargs):
    for val in args:
        print(f"{val}")
    for key,value in kwargs.items():
        print(f"{key}:{value}")
# print_details(1,2,3,4,"Binal",name="Binal",age="22",country="india")

#Return statements
def multiply(a,b):
    return a*b
multiply(2,3)

##return multiple parameters
def multiply(a,b):
    return a*b,a
multiply(2,3)

#EXAMPLES:

##Ex-1 -> Temperature conversion
def convert_temperature(temp,unit):
    if unit=='C':
        return temp * 9/5 + 32  ## celsius to fehrenhit
    elif unit=='F':
        return (temp-32)*5/9    ## fehrenhit to celsius
    else:
        return None
print(convert_temperature(25,'C'))   #77
print(convert_temperature(77,'F'))   #25

##Ex:2 -> Password strength checker
def is_strong_password(password):
    if len(password<8):
        return False
    if not any(char.isdigit() for char in password ):
        return False
    if not any(char.islower() for char in password ):
        return False
    if not any(char.isupper() for char in password ):
        return False
    if not any(char in '!@#$%^&*()' for char in password ):
        return False
    return True
print(is_strong_password("weakPed"))
print(is_strong_password("str0ngPwd!"))

#Ex-3: -> Calculate the total cost of items in a shopping carts
def calculate_total_cost(cart):
    total_cost=0
    for item in cart:
        total_cost+=item['price']*item['quantity']
    return total_cost
## cart data
cart=[
    {'name':'apple','price':0.5,'quantity':4},
    {'name':'Banana','price':0.3,'quantity':6},
    {'name':'Orange','price':0.7,'quantity':3}
]
total_cost=calculate_total_cost(cart)
print(total_cost)                            ##5.89999999995

##Ex:4 ->  Check if a string is palindrome
def is_palindrome(s):
    s=s.lower().replace(" ","")
    return s[::-1]
print(is_palindrome("A man a plan a canal panama"))   ##True
print(is_palindrome("Hello"))                         ##False

##Ex:5 -> Calculate the factorials of a number using recursion
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(6))                 ##720

##Ex:6 -> Function to read a file and count the frequency of each word
def count_word_frequency(file_path):
    word_count={}
    with open(file_path,'r') as file:
        for line in file:
            words=line.split()
            for word in words:
                word=word.lower().strip('.,!?;:"\'')
                word_count[word]=word_count.get(word,0)+1
    return word_count
filepath='.txt'
count_word_frequency(filepath)
count_word_frequency

##EX:7 -> Validate email address
def is_valid_email(email):
    pattern=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None
print(is_valid_email("test@example.com"))        ##True
print(is_valid_email("invalid.email"))           ##False