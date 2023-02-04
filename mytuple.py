# uses ('tuple') instead of ['list']
my_info = ("Danny", 24, "Bad Ass")
# accessing
print(my_info)
print(my_info[0])
print(my_info[1])
print(my_info[-1])
# ERROR: my_info[0] = "Daniel"
# unpacking
name, age, occupation = my_info
print(name)
print(age)
print(occupation)
# one element tuple
one_element_tuple = ("element",)