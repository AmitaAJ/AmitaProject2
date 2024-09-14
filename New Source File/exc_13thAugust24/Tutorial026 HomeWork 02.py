# Create a program , take 2 inputs from the user num1, num2 and give them
# max
# pow num1 to num2
# sub, mul, sum, div.
# Format your out with f{""}
# Methode 1 - Convert str to int , in f function
num_001 = input("Enter the value of Number 01")
num_002 = input("Enter the value of Number 02")
print(num_001)
print(num_002)
print(type(num_001))
print(type(num_002))
# print(f"{Table}*1={Table * 1}")
print(f"Maximum number out of {num_001} and {num_002} is ={max(num_001, num_002)}")
print(f"Minimum number out of {num_001} and {num_002} is ={min(num_001, num_002)}")
print(f"Power of {num_001} and {num_002} is = {pow(int(num_001),int(num_002))}")
print(f"Addition of {num_001} and {num_002} is ={int(num_001) + int(num_002)}")
print(f"Multiplication of {num_001} and {num_002} is ={int(num_001) * int(num_002)}")
print(f"Division of {num_001} and {num_002} is ={int(num_001) / int(num_002)}")
print(f"Subtraction of {num_001} and {num_002} is ={int(num_001) - int(num_002)}")
# print('---------------------------------------------------------')
# Methode 1 - Convert str to int , in f function
num_001 = int(input("Enter the value of Number 01"))
num_002 = int(input("Enter the value of Number 02"))
print(num_001)
print(num_002)
print(type(num_001))
print(type(num_002))
print(f"Maximum number out of {num_001} and {num_002} is ={max(num_001, num_002)}")
print(f"Minimum number out of {num_001} and {num_002} is ={min(num_001, num_002)}")
print(f"Power of {num_001} and {num_002} is = {pow(num_001,num_002):.4f}")
print(f"Addition of {num_001} and {num_002} is ={num_001 + num_002}")
print(f"Multiplication of {num_001} and {num_002} is ={num_001 * num_002}")
print(f"Division of {num_001} and {num_002} is ={num_001 / num_002}")
print(f"Subtraction of {num_001} and {num_002} is ={num_001 - num_002}")