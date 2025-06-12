"""
*********
 ******* 
  *****  
   ***   
    *    
"""

"""
i = 0, 2*n - (2*i + 1) = 10 - 1 = 9
i = 1, 2*n - (2*i + 1) = 10 - 3 = 7
i = 2, 2*n - (2*i + 1) = 10 - 5 = 5
i = 3, 2*n - (2*i + 1) = 10 - 7 = 3
i = 4, 2*n - (2*i + 1) = 10 - 9 = 1
"""

# Method 1:
n = int(input("Enter the number of lines: "))
for i in range(0, n):
    for j in range(0, i):
        print(" ", end="")
    
    for j in range(0, 2*n - (2*i + 1)):
        print("*", end="")

    for j in range(0, i):
        print(" ", end="")
    print()

# Method 2:
"""
n = int(input("Enter the number of lines: "))

for i in range(n, 0, -1):
    for j in range(0, n - i):
        print(" ", end="")
    
    for j in range(0, 2*i-1):
        print("*", end="")

    for j in range(0, n - i):
        print(" ", end="")
    print()
"""