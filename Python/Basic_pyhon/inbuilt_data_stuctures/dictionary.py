#store data in key-value pair
#unoredered collection of items
#value can be any types
#key must be unique and immutable

#creating dictonary
empty_dict={}
print(type(empty_dict))
empty_dict=dic{}
empty_dict

student={"name":"binal","age":22,"grade":25}
student
print(type(student))
##error
student={"name":"binal","age":22,"name":23} ### name:binal 0r 23 also and replce with last value
student

#Accessing dictionary elements
student={"name":"binal","age":22,"grade":"A"}
student
print(student["grade"])
print(student["age"])
##Accessing using get() method
print(student.get("grade"))
print(student.get("last_name"))
print(student.get("last_name","not available")) ## give bydefault value

#Modifying dict elements
##dict are mutable , so you can add update and delete an elemnets 
print(student)
student["age"]=23            ## update the value of key (age)
student
student["address"]="india"   ## added new key and value
student
del student["grade"] 
student        ## delete the key and value pair by using del

# Dict methods
keys=student.keys()       ## get all keys
keys
values=student.values()    ## get all values
values
items=student.items()       ## get all  key value pair
items

# Shallow copy
student_copy=student
student
student_copy
student["name"]="binal2"
student
student_copy 

student_copy1=student_copy()    ## shallow copy
student_copy1
student

student["name"]="binal3"
student
student_copy1

# Iterating over dict
##you can use loop to iterate over dict , keys, values or items

## iterating over keys
for keys in student.keys():
    print(keys)

## iterating over values
for keys in student.values():
    print(values)

## iterating over keys and values
for key,value in student.items():
    print(f"{key}:{value}")

# Nested dic
students={
    "student1":{"name":"binal","age":22},
    "student2":{"name":"bhoomi","age":21}
}
students

## Accesing nested dic
print(students["student2"]["name"])
print(students["student2"]["age"])

students.items()

## iterating over netsef dic
for student_id,student_info in students.items():
    print(f"{student_id}:{student_info}")
    for key,value in student_info.items():
         print(f"{key}:{value}")
        
# dict comphrehension
squares={x:x**2 for x in range(5)}
squares

##conditional dict comphrehension
evens={x:x**2 for x in range(10) if  x%2==0}
evens

### use a dict to count the frequency of elements in list
numbers=[1,2,2,3,3,3,4,4,4,4]
frequency={}
for number in numbers:
    if number in frequency:
        frequency[number]+=1
    else:
        frequency[number]=1
print(frequency)

## Merge two dict in one
dict1={"a":1,"b":2}
dict2={"b":3,"d":4}
merge_dict={**dict1,**dict2}
merge_dict