"""
for identifier in range(start=0, stop, step=1):
    pass
"""

# for i in range(0, 10):
#     print(i+1)

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i, "x", j, "=", i*j)
#     print()

"""
while (condition):
    pass
    
The loop terminates, whenever the condition is reached.
"""

"""
i = 50
while (i >= 0):
    if (i == 20):
        # break
        i -= 1
        continue
    print(i)
    i -= 1
"""

ch = 'A'

# for i in range(ord(ch), ord('Z')):
#     if (chr(i) == 'J'):
#         continue
#     print(chr(i))

for i in range(ord(ch), ord('Z'), 3):
    if (chr(i) == 'J'):
        continue
    print(chr(i))
