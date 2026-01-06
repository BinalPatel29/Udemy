# mutable
# different datatypes collection
lst=[]
print(type(lst))

# add elements of the list
name=["binal","bhoomi",1,2,3]
print(name)

#accessing list element
fruits=["apple","kiwi","banana","cherry"] 
print(fruits[0])
print(fruits[-1])
print(fruits[2])
print(fruits[1:3])
print(fruits[1:])

# modify the list element
fruits
fruits[1]="grapes"
print(fruits) 

fruits[1:]="grapes"
print(fruits)

fruits

#list methods
fruits.append("watermalon")  ## add an item
print(fruits)

fruits=["apple","kiwi","banana","cherry"]

fruits.remove("kiwi")  ## remove an item in first occurance
print(fruits)

fruits=["apple","kiwi","banana","cherry"]
fruits.insert(1,"orange")   ## insert an item in specific index
print(fruits)

pop_fruits=["apple","kiwi","banana","cherry"]
pop_fruits=fruits_pop() ## remove and return the last item ("cherry")
print(pop_fruits)
print(fruits)

fruits
index=fruits.index("banana")
print(index)

fruits.insert(2,"banana")
fruits.count("banana")    ## count the item present in list
print(fruits)

fruits.sort()  ## sorting an items in ascending order
fruits

fruits.reverse()   ## reverse an items
fruits   

fruits.clear()   ## remove all items in the list
fruits

#slicing list
numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers)
print(numbers[2:5])
print(numbers[2:])
print(numbers[:2])
print(numbers[::2])
print(numbers[::-1])
print(numbers[::-2])

#iterating over list
fruits=["apple","kiwi","banana","cherry"]
for fruit in fruits:
    print(fruit)

for index,fruit in enumerate(fruits):
    print(index,fruit)

# list comprehension
lst=[]
for x in range(10):
    lst.append(x**2)
print(lst)

[i**2 for i in range(10)]

#Basic syntax             [expression for item in iterable]
square=[num**2 for num in range(10)]
print(square)

#With conditional logic   [expression for item in iterable if condition]
lst=[]
for i in range(10):
    if i%2==0:
        lst.append(i)
print(lst)

even_num=[num for num in range(10) if num%2==0]
print(even_num)

#nested list comphrension 
lst1=[1,2,3]
lst2=["a","b","c"]

pair=[[i,j] for i in lst1 for j in lst2]
print(pair)

# REAL WORLD EXAMPLES

### EXAMPLE-1 -> mange a to do list
    ## Create a to do list to keep track of task
    to_do_list=["buy Groceries","Clean the house","Pay the bills"]
    to_do_list
    ##adding a task
    to_do_list.append("schedule meeting")
    to_do_list.append("go for a run")
    to_do_list
    ##remove a completed task
    to_do_list.remove("Clean the house")
    to_do_list
    ##checking if a task in a list
    if "Pay the bills" in to_do_list:
        print("don't forget to pay the utillity bills")
    print("to do list remaining")
    for task in to_do_list:
        print(f"-{task}")

### EXAMPLE-2 ->organizing studesnt grades
    ## create a list to store and calculate average grades for students
    # organizing student grades
    grades=[85,92,78,90,88]
    grades
    #adding a new grade
    grades.append(95)
    grades
    # calculating the average grade
    average_grade=sum(grades)/len(grades)
    average_grade      #print(f"average grade: {average_grade:.2f}")
    # finding hte highest and lowest grades
    highest_grade=max(grades)
    highest_grade
    lowest_grade=min(grades)
    lowest_grade

### EXAMPLE-3 -> managing an inventory
    #use a list to manage inventory items in a store
    ## managing an inventory
    inventory=["apples","bananas","oranges","grapes"]
    inventory
    ##adding a new item
    inventory.append("strawberries")
    inventory
    ##removing an item
    inventory.remove("bananas")
    inventory
    ##checking if an item in a list
    item="oranges"
    if item in inventory:
       print(f"{item} are in stock.")
    else:
       print(f"{item} are out of stock.")
    ##printing the inventory
    print("inventory list:")
    for item in inventory:
        print(f"-{item}") 

### EXAMPLE-4 -> Colletcing user feedback
    #use a list to collect and anlyze user feedback
    feedback=["Great service","Very satisfied","Could be better","Exellent experience"] 
    feedback
    #adding new feedback
    feedback.append("Not happy with service")
    feedback
    #counting specific feedback
    positive_feedback_count=sum(1 for comment in feedback if "great" in comment.lower() or "excellent" in comment.lower())
    positive_feedback_count
    #printing all feedback
    print("User feedback:")
    for comment in feedback:
        print(f"-{comment}")