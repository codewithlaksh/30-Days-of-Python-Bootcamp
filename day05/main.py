"""
if (condition):
    # code
elif (condition):
    # code
else:
    # code
"""

age = int(input("Enter your age: "))

# if (age >= 18):
#     print("You are eligible for a driving license.")
# else:
#     print("You are not eligible for a driving license.")

"""
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter another number: "))

if (a > b and a > c):
    print("a is greater than b & c")
elif (b > a and b > c):
    print("b is greater than a & c")
else:
    print("c is greater than a & b")
"""

if (age >= 18 and age < 50):
    print("You can drive!")
else:
    if (age > 50):
        print("You can drive but drive carefully!")
    else:
        print("You cannot drive!")
