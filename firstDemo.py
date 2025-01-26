
"""
This is first lecture in Rhaul sheety course in python
"""
d=3
a, b, c = 10, "Momo", 15.5
Str = "Hello, My friend"

# Adding string to another
print(Str + " " + b)
print("{} is {}".format("Your value", 25))

print(d)
print(a)
print(a+int(c))

"""
List items are ordered, changeable, and allow duplicate values.
"""
List = [1,2,4,6,8,9]

#-1 refers to the last item, -2 refers to the second last item etc.
print(List[-1])
print(List[-2])

"""
You can specify a range of indexes by specifying where to start and where to end the range.
The search will start at index 2 (included) and end at index 5 (not included).
"""
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[2:5])

#if u leave the first index range, it will take the first one by default
print(this_list[:4])

# By leaving out the end value, the range will go on to the end of the list:
print(this_list[5:])

"""
The length of the list will change when the number of
items inserted does not match the number of items replaced.
"""
this_list[2:4] = ["soso", "koko", "lolo"]
print(this_list)

# Adding number to the list at a specific index
List.insert(2,77)
print(List)

# Adding number to the list at the end
List.append(10)
print(List)

# Updating values
List[1]=600
print(List)

# Deleting values
del List[1]
print(List)

"""
Tuple items are ordered, unchangeable, and allow duplicate values.

When we say that tuples are ordered,
it means that the items have a defined order, and that order will not change.

Tuples are unchangeable, meaning that we cannot change,
add or remove items after the tuple has been created.
"""
this_tuple = ("apple", "banana", "cherry", "apple", "cherry")
print(this_tuple)
print(type(this_tuple))

"""
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered(in python 3.7 ordered but less are not)
 ,changeable and do not allow duplicates.
"""
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(this_dict["brand"])
print(type(this_dict))

