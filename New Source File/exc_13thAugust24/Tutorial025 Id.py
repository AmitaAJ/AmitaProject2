# The id() function returns a unique id for the specified object.
# All objects in Python has its own unique id.
# The id is assigned to the object when it is created.
# The id is the object's memory address, and will be different for each time you run the program.
# (except for some object that has a constant unique id, like integers from -5 to 256)

Age = 95
Age2 = 95
print(id(Age))
print(id(Age2))

print('------------------------')

New_Age = 65
New_Age2 = 85
print(id(New_Age))
print(id(New_Age2))