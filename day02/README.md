# Day 2: First Program

Youtube Video URL: [https://www.youtube.com/watch?v=yyZ_IQflqSE](https://www.youtube.com/watch?v=yyZ_IQflqSE)

Hello everybody, today is the 2nd day of our 30 days python bootcamp series. 

In this video, we will write our first program in python.

## Installing the Python extension
1. Go to the extensions inside vscode & search for **Python** extension. You will find official extension by **Microsoft**.
2. Manual Installation (optional): [Download](https://marketplace.visualstudio.com/items?itemName=ms-python.python) the extension from market place & install manually.

## First Program
```python
print("Hello World")
```

- Escape sequence characters:
    - `\t` adds a tab character
    - `\n` adds a new line character
    - `\\` adds a single backward slash (`\`)
    - `\'` adds a single quote
    - `\"` adds a double quote

- Comments: Comments are the statements which are not executed by our Python interpreter.

- About the `end` argument in print statement:
    - The `end` argument in the print statement defaults to `\n` (new line) character. So, when we write multiple print statements, the cursor moves to the next line, instead of staying in the same line.

    - To avoid this behaviour, we add `end=" "`, which adds a space at the end of each print statement, instead of moving cursor to the next line.

    Example:
    ```python
    print("Lakshyaraj", end=" ")
    print("is a", end=" ")
    print("good boy")
    ```

    Output:
    Lakshyaraj is a good boy