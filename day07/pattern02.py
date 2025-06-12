"""
    *    
   ***   
  *****  
 ******* 
*********
"""

n = int(input("Enter the number of lines: "))

"""
n = 5
i = 0, n - i - 1 = 4
i = 1, n - i - 1 = 3
i = 2, n - i - 1 = 2
i = 3, n - i - 1 = 1
i = 4, n - i - 1 = 0
"""

for i in range(0, n):
    for j in range(0, n - i - 1):
        print(" ", end="")
    
    for j in range(0, 2*i+1):
        print("*", end="")

    for j in range(0, n - i - 1):
        print(" ", end="")
    print()
