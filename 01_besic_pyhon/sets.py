##collection of unique items (not allow duplicate elemnets)
##unordered

#create a set
my_set={1,2,3,4,5}
my_set
print(type(my_set))

my_set=set([1,2,3,4,5,6])
my_set
print(type(my_set))

my_empty_set=set([1,2,3,6,5,4,5,6]) ##give all items in once in output 
my_empty_set

#Basic sets opertion
##Adding and Removing an elements
my_set.add(6)
my_set
my_set.add(7)     ##{1,2,3,4,5,6,7}
my_set
my_set.add(7)     ##{1,2,3,4,5,6,7} 7 add only one time 
my_set

##Remove the elements from a set
my_set.remove(3)
my_set

my_set.discard(10)   ##discard->remove an elemnet from aset if it's member
my_set

my_set.pop()
my_set

##clear all the elements
my_set.clear()
my_set

#set membership test
my_set={1,2,3,4,5}
print(3 in my_set)
print(10 in my_set)

#mathemetical operation
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}

##union
union_set=set1.union(set2)
union_set

##intersection
intersection_set=set1.intersection(set2)
intersection_set

set1.intersection_update(set2)
set1