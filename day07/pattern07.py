"""
E
D E
C D E
B C D E
A B C D E
"""

ch = 'E'

n = int(input("Enter the number of lines: "))
for i in range(0, n):
    for j in range(ord(ch) - i, ord('E') + 1):
        print(chr(j), end=" ")
    print()

