# String Function

Name = "Pramod"
print(Name)
print(type(Name))
print(Name.upper())
print(Name.lower())
print(len(Name))

a = "90"
print(type(a))

b = 90
print(type(b))

Big_Name = "This is a Big Line"
print(Big_Name)
print(type(Big_Name))

# new_name = Big_Name + 1 # ---> This is not possible because we cant add string + int
# print(new_name)

# Method 1 is add a double quote for 1 like "1" OR
# Convert int into str like str(1)

new_name = Big_Name + str(1)
print(new_name)

new_name = Big_Name + "1"
print(new_name)

# Concatenation
First_Name = "Amita"
Middle_Name = "Anant"
Last_Name = "Jadhav"
My_Full_Name = (First_Name + Middle_Name + Last_Name)
print(My_Full_Name)


How_many_planes_do_i_have = None
print(type(How_many_planes_do_i_have)) # Type is NoneType

# Null concept not aailable in python it is there in java
