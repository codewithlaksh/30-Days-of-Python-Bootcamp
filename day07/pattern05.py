"""
1        1
12      21
123    321
1234  4321
1234554321
"""

n = int(input("Enter the number of lines: "))
initial_spaces = 2*n - 2

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")

    for j in range(0, initial_spaces):
        print(" ", end="")

    for j in range(i, 0, -1):
        print(j, end="")
    
    initial_spaces -= 2
    print()