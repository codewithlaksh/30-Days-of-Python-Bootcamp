# Day 8: Strings & String Methods

Welcome to **Day 8** of the Python Bootcamp! Today’s focus is on **strings** and **string methods**—foundational tools in Python used for text manipulation.

---

## String Declaration

Strings in Python can be defined using:
```python
string1 = "CodeWithLaksh"
string2 = 'CodeWithLaksh'
string3 = '''CodeWithLaksh'''
```

All of the above are valid string declarations and produce the same result.

---

## Escape Sequences

- `\n` – New line  
- `\t` – Tab  
- `\b` – Backspace  
- `\'` – Escaped single quote

Example:
```python
str1 = 'Lakshyaraj\'s favourite programming language is Python'
```

---

## Length of a String

```python
len(string)  # Returns number of characters
```

---

## String Slicing

```python
string[0:5]    # From index 0 to 4
string[:5]     # From start to index 4
string[0:]     # From index 0 to end
string[::-1]   # Reversed string
string[::2]    # Every second character
string[-1:-10:-1]  # Slicing in reverse with negative indices
```

---

## Character Access

```python
string[4]      # 5th character
string[-3]     # 3rd character from the end
```

---

## Search & Locate

- `.find()` returns index of **first occurrence** or `-1` if not found.
- `.index()` is similar, but raises **ValueError** if not found.

```python
string.find('C')    # 0
string.find('q')    # -1

string.index('de')  # Valid
# string.index('q') # Raises ValueError
```

---

## Splitting Strings

```python
str2 = 'Lakshyaraj,Mayank,Ivy,Sahil'
str2.split(',')        # Splits into list
str2.split(',', 1)     # Splits only once
```

---

## String Case Methods

```python
username.upper()      # Uppercase
username.lower()      # Lowercase
username.swapcase()   # Swap cases
```

---

## Validation Methods

```python
course_title.isupper()    # True if all uppercase
course_title.islower()    # True if all lowercase
course_title.isalnum()    # True if only letters and numbers
```

---

## Title Case & Trimming

```python
course_title.title()         # Converts to title case
course_title.strip(" ")      # Removes leading/trailing spaces
```

---

## Start & End Check

```python
course_title.startswith("Wel")   # True
course_title.endswith("camp")    # True
```

---

## Count & Partition

- `.count('x')` – Returns number of times 'x' appears
- `.partition(' ')` – Splits into 3-part tuple: (before, match, after)

---

## String Traversal

1. **For Loop with Membership**
   ```python
   for char in course_title:
       print(char)
   ```
2. **Index-based Traversal**
   ```python
   for i in range(len(course_title)):
       print(course_title[i])
   ```