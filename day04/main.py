"""
Oprators:
1. Arithmetic operators: +, -, *, /, **, %, //
2. Assignment operators: =, +=, -=, *=, /=, =**, %=, //=, >>=, <<=
3. Bitwise operators: &, |, ~, ^, >>, <<
4. Comaprison operators: ==, !=, <, >, <=, >=
5. Logical operators: and, or, not
6. Membership operators: in, not in
7. Identity operators: is, is not
"""

"""
a = 64
b = 36

print("a + b =", a+b)
print("a - b =", a-b)
print("a * b =", a*b)
print("a / b =", a/b)
print("a ** b =", a**b)
print("a % b =", a%b)
print("a // b =", a//b)

c = 8

c += a
print(c)
"""

"""
print(3 & 5) 
print(3 | 5) 

d = 5 # 0101
e = d << 2 # 010100
f = 10 >> 2 # 000101

print(e)
print(f)
"""

"""
  011
& 101
-----
  001
"""
"""
  011
| 101
-----
  111
"""

a = 24
b = 13

# print(a < b)
# print(a > b)
# print(a == b)
# print(a != b)
# print(a <= b)
# print(a >= b)

# and, or, not
# print(a < b and a > b)
# print(a < b or a > b)
# print(not (a < b))

# print("q" in "CodeWithLaksh")
# print("q" not in "CodeWithLaksh")
# print(1 in {1: "One", 2: "Two", 3: "Three"})

a = 49
b = 34

print(a is b)
print(a is not b)