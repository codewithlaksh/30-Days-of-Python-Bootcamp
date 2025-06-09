"""
Variables: These are the containers which store specific values.

Rules:
1. Variables cannot start with a number. Ex: 99w is invalid
2. Do not use reserved keywords or functions as variable names. Ex: class, sum
3. Variables are case sensitive. Ex: a & A are different in python
4. Variables cannot contain special characters other than underscores (_).
5. Variables can contain numbers between them.
"""

a = 64
b = 36

# print("The value of a is", A) # NameError
# print("The value of a is", a)
# print("The value of b is", b)

"""
Datatypes: int, float, bool, str, list, tuple, dict, set, complex

Mutable datatypes (allow item assignment): list, dict, set
Immutable datatypes (do not allow item assignment): int, float, bool, str, tuple, complex
"""

# print(type(a))
# print(type(45.3))
# print(type(True))
# print(type("Hello World"))
# print(type([1, 2, 3, 4, 5, 6]))
# print(type((1, 2, 3, 4, 5, 6)))
# print(type({1, 2, 3, 4, 5, 6}))
# print(type({1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six"}))
# print(type(4 + 8j))

"""
Typecasting is the conversion of one datatype to another datatype
"""

c = "A"
# print(ord(c))

d = 43
# print(type(d))
# print(type(str(d)))
# print(chr(d))

"""
We cannot cast int, float, bool & complex datatypes into list/tuple/dict/set, also not str into dict.
"""

# print(list(34)) # TypeError
# print(dict("Lakshyaraj")) # TypeError

print(list("Lakshyaraj"))
