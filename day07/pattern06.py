"""
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
"""

n = int(input("Enter the number of lines: "))
initial_spaces = 0

for i in range(0, n):
    for j in range(1, n - i + 1):
        print("*", end="")

    for j in range(0, initial_spaces):
        print(" ", end="")

    for j in range(1, n - i + 1):
        print("*", end="")
    
    initial_spaces += 2
    print()

initial_spaces = 2*n - 2

for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end="")

    for j in range(0, initial_spaces):
        print(" ", end="")

    for j in range(i, 0, -1):
        print("*", end="")
    
    initial_spaces -= 2
    print()