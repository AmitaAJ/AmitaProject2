# Home Work Task | 13th Aug 2024
# Task #1
# Home Can you create a Program I will give you number(userinput and print table)
# f"{}" String format concept
# User input - num int -> 10, 100, -1, 2, 3.14 -> input
# 9x1 = 9
# 9x2 = 18... till 10

user_number01 = int(input("The User input number is , "))
print(user_number01)
print(f"{user_number01}*01={user_number01 * 1}")
print(f"{user_number01}*02={user_number01 * 2}")
print(f"{user_number01}*03={user_number01 * 3}")
print(f"{user_number01}*04={user_number01 * 4}")
print(f"{user_number01}*05={user_number01 * 5}")
print(f"{user_number01}*06={user_number01 * 6}")
print(f"{user_number01}*07={user_number01 * 7}")
print(f"{user_number01}*08={user_number01 * 8}")
print(f"{user_number01}*09={user_number01 * 9}")
print(f"{user_number01}*10={user_number01 * 10}")

# Above function is used to print a output for numbers 10, 100, -1, 2
# Float number 3.14 will give error as ValueError: invalid literal for int() with base 10: '3.14'

# For Float number we can conver our string into float
user_number01 = float(input("The User input number is , "))
print(user_number01)
print(f"{user_number01}*01={user_number01 * 1}")
print(f"{user_number01}*02={user_number01 * 2}")
print(f"{user_number01}*03={user_number01 * 3}")
print(f"{user_number01}*04={user_number01 * 4}")
print(f"{user_number01}*05={user_number01 * 5}")
print(f"{user_number01}*06={user_number01 * 6}")
print(f"{user_number01}*07={user_number01 * 7}")
print(f"{user_number01}*08={user_number01 * 8}")
print(f"{user_number01}*09={user_number01 * 9}")
print(f"{user_number01}*10={user_number01 * 10}")
# So above float function will print following output,
# The User input number is , 3.14
# 3.14
# 3.14*01=3.14
# 3.14*02=6.28
# 3.14*03=9.42
# 3.14*04=12.56
# 3.14*05=15.700000000000001
# 3.14*06=18.84
# 3.14*07=21.98
# 3.14*08=25.12
# 3.14*09=28.26
# 3.14*10=31.400000000000002
