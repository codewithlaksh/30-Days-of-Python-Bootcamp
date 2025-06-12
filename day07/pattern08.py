"""
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
"""

n = int(input("Enter the number of lines: "))
start = 0
for i in range(0, n):
    if (i % 2 == 0):
        start = 1
    for j in range(0, i+1):
        print(start, end=" ")
        start = 1 - start
    print()