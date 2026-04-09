# ordered collection of an items
# immutable

#creatind a tuple
tpl=()
print(tpl)
print(type(tpl))

lst=list()
print(type(lst))
tpl=tuple()
print(type(tpl))

numbers=tuple([1,2,3,4,5,6,7])
numbers
list((1,2,3,4,5))      ##(())->list

mixed_tuple=(1,"hello",True)
mixed_tuple

#Accessing tuple element
numbers
numbers[0]
numbers[-1]
numbers[0:4]
numbers[::]
numbers[::-1]

#Tuple operation
concatenation_tuple=numbers + mixed_tuple
print(concatenation_tuple)

mixed_tuple * 3
numbers * 3

#immutable nature of tuples
lst=[1,2,3,4,5]
lst
lst[1]="a"
lst
numbers[1]="a"   ## not change value once assign

#Tuple methods
numbers
print(numbers.count(1))
print(numbers.index(3))

#Packing and Unpacking Tuple
packed_tuple=(1,"hello",3.14)
packed_tuple

#unpacking a tuple
a,b,c=packed_tuple
print(a)
print(b)
print(c)

#unpacking with *
numbers=(1,2,3,4,5,6)
first,*middle,last=numbers
print(first)
print(middle)
print(last)

#Nested tuple
##Nested list
lst=[[1,2,3,4],[6,7,8,9],[1,"hello",3.14,"c"]]
lst[0][0:3]
lst=[[1,2,3,4],[6,7,8,9],(1,"hello",3.14,"c")]
lst[2][0:3]

nested_tuple=((1,2,3),("a","b","c"),(True,False))
nested_tuple[0]
nested_tuple[1][2]

#Iterating over nested tuple
nested_tuple=((1,2,3),("a","b","c"),(True,False))
for sub_tuple in nested_tuple:
    for item in sub_tuple:
        print(item,end=" ")
    print()
