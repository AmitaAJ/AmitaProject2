# How To Convert a string into intiger.
# To do that just add input() funtion inside int()function such as int(input())

num_001 = int(input("Enter the value of Number 01"))
num_002 = int(input("Enter the value of Number 02"))

print(type(num_001))
print(type(num_002))

print("Addition / Sum is ", num_001 + num_002)
print("Multiplication is ", num_001 * num_002)
print("Division is ", num_001 / num_002)
print("Subtraction is ", num_001 - num_002)

# Division is  1.7567567567567568
# Question is - We used int function still division output getting into float.
# Becasue - Python is a very smart langauge , diision is always in the form of float and decimal value.
# therefore even if it is intiger in case of di it always float.