string = "CodeWithLaksh"
string2 = 'CodeWithLaksh'
string3 = '''CodeWithLaksh'''

# print(type(string))
# print(type(string2))
# print(type(string3))

# str1 = "Lakshyaraj\nis a good boy"
# str1 = "Lakshyaraj\tis a good boy"
# str1 = "Lakshyaraj\bis a good boy"
# str1 = 'Lakshyaraj\'s favourite programming language is Python'
# print(str1)

# len1 = len(string2)
# print(string2, "is a", len1, "letter word.")

# print(string[0:5])
# print(string[:5])
# print(string[0:])
# print(string[0:15])

# print(string[::-1])
# print(string[::-2])
# print(string[::2])

# print(string[-1:-10:-1])

# print(string[4])
# print(string[-3])
# print(string[0])
# print(string[-1])

# find method returns the index where the element is present, -1 otherwise
# returns index of first occurrence

# print(string.find('q')) # -1
# print(string.find('C')) # 0

# split method returns a list based on the sep value.
# maxcount in split refers to the maximum count of sep by which we will split the string

# str2 = 'Lakshyaraj,Mayank,Ivy,Sahil'
# print(str2.split(','))
# print(str2.split(',', 1))
# print(str2.split(',', 2))

# index returns the index number at which substring starts, else it raises ValueError
# returns index of first occurrence

# print(string.index('q')) # ValueError
# print(string.index('de'))

username = "Laksh20092"

# upper method changes the string to uppercase
# print(username.upper())

# lower method changes the string to lowercase
# print(username.lower())

# swapcase method swaps uppercase to lowercase & lowercase to uppercase letter
# print(username.swapcase())

course_title = "Welcome to my 30 days of python bootcamp"

# isupper returns false if the entire string is not in uppercase letters, else true
# print(course_title.isupper())

# islower returns false if the entire string is not in lowercase letters, else true
# print(course_title.islower())

# Return True if the string is an alpha-numeric string, False otherwise.
# print(course_title.isalnum())

# title method returns the string in title case (first letter each word is in uppercase)
# print(course_title.title())


# print(course_title.rstrip(" "))
# print(course_title.lstrip(" "))
# print(course_title.strip(" "))

# print(course_title.startswith("Wel"))
# print(course_title.startswith("Qel"))

# print(course_title.endswith("camp"))
# print(course_title.endswith("qamp"))
# count returns the number of occurrences of the substring in the string.
# print(course_title.count('W'))

# partition returns a tuple of 3 elements with the string by which the main string has been partitioned
# if the element is not present, it returns a tuple having the entire string at first index & two empty strings at the end

# print(course_title.partition(" ")) # ('Welcome', ' ', 'to my 30 days of python bootcamp')
# print(course_title.partition("q")) # ('Welcome to my 30 days of python bootcamp', '', '')

# String traversal using for loop

# 1. Directly accessing using membership
# for i in course_title:
#     print(i)

# 2. Using indexing
for i in range(len(course_title)):
    print(course_title[i])
