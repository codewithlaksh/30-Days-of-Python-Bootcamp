"""
    1    
   121   
  12321  
 1234321 
123454321
"""

n = int(input("Enter the number of lines: "))
for i in range(0, n):
    for j in range(0, n - i - 1):
        print(" ", end="")

    num = 1
    break_point = (2*i + 1) // 2
    for j in range(0, 2*i + 1):
        print(num, end="")
        if (j < break_point):
            num += 1
        else:
            num -= 1

    for j in range(0, n - i - 1):
        print(" ", end="")
    
    print()
