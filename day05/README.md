# Day 5: Conditionals in Python

- Syntax:
    ```python
    if (condition):
        # code
    elif (condition):
        # code
    else:
        # code
    ```

## if statement
A simple if statement works on the following principle:

- Execute the block of code inside the if statement if the expression evaluates to `True`.
- Ignore the block of code inside the if statement if the expression evaluates to False and return to the code outside the if statement.

## if-else statement
An if......else statement works on the following principle:

- Execute the block of code inside the if statement if the expression evaluates to `True`. After execution, return to the code outside of the `if......else` block.
- Execute the block of code inside the else statement if the expression evaluates to False. After execution, return to the code outside of the `if......else` block.

## elif statement
An elif statement works on the following principle:

- Execute the block of code inside the `if` statement if the initial expression evaluates to `True`. After execution, return to the code outside the `if` block.
- Execute the block of code inside the first `elif` statement if the expression inside it evaluates to `True`. After execution, return to the code outside the `if` block.
- Execute the block of code inside the second `elif` statement if the expression inside it evaluates to `True`. After execution, return to the code outside the `if` block.
- Execute the block of code inside the nth `elif` statement if the expression inside it evaluates to `True`. After execution, return to the code outside the `if` block.
- Execute the block of code inside the `else` statement if none of the expressions evaluate to `True`. After execution, return to the code outside the `if` block.
