"""
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
"""

n = int(input("Enter the number of lines: "))
initial_spaces = 2*n - 2

for i in range(1, 2*n):
    if (i < n):
        stars = i
    else:
        stars = 2*n - i    

    for j in range(1, stars+1):
        print("*", end="")

    for j in range(1, initial_spaces+1):
        print(" ", end="")

    for j in range(1, stars+1):
        print("*", end="")

    if (i < n):
        initial_spaces -= 2
    else:
        initial_spaces += 2

    print()