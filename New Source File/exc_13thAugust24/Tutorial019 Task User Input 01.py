# User Input -> User will enter a input and then system will print its output.
# User Input -> Datatype of input() function is always String [str]

# Task :- Take a user input a , b and calculate the sum , mul , div , sub
# Calculator Program

num_001 = input("Enter the value of Number 01")
num_002 = input("Enter the value of Number 02")

print(type(num_001))
print(type(num_002))

print("Addition / Sum is ", num_001 + num_002)
print("Multiplication is ", num_001 * num_002)
print("Division is ", num_001 / num_002)
print("Subtraction is ", num_001 - num_002)

# The above function will give you an error because we are using the input() function.
# By default input() functions type is str [Strintg]
# 2 strings can't be added, mult, divided, or subtracted,
# to do mathematical expression we need integer data type.
# In the case of Add / Sum -> Two strings are Concatenate therefore getting out as 5040 but it can't add.
# So we need to do mathematical calculations we need to convert a string into an integer value.
# to do that just add input() funtion inside int()function such as int(input())
