Comments
========

It's a good idea to add comments to your code if what you are doing may be difficult to understand or if you need to leave a reminder to make a change at a later time. Python has two types of comments, docstrings and line comments.
Docstrings allow you make multi-line comments. Docstrings are typically found near the top of Python files and at the top of functions and classes (we'll talk more about these later). Docstrings are used by Python to provide help output and usually describe what a python module, function or class does, what input is needed and what the results will be if the code is run.
Consider the following lines of code from the previous lesson, basics.py.

```
    '''
    The following code shows you how to accept input from a user, do something with that input and print out a response.
    '''
    name = input("What is your name? ")
    age = input("How old are you "+name+"? ")
    print("Hello, ", name, ". You are ", age, " years old.")
    # We convert age to an int before we multiply it by 10.
    print(age," * ", 10, " = ", (int(age) * 10))
    print("The first character of your name is ",name[0])
    print("Is your age == 11,", int(age) == 11)
```

If you were to start Python and import this file, basics would run. And then if you type help(basics) you would see the docstring for this file.

```
        >> import basics
        What is your name? John
        How old are you asdf? 2
        Hello,  asdf . You are  2  years old.
        2  *  10  =  20
        The first character of your name is  a
        Is your age == 11, False
        >>> help(basics)

        Help on module basics:

    NAME
        basics - The following code shows you how to accept input from a user, do something with that input and print out a response.

    DATA
        age = '2'
        name = 'John'

    FILE
        /Users/scottumsted/Projects/Workspaces/git_workspace/python_class/class1-basics/basics.py
```

Another type of comment is the line comment. Line comments are indicated using the # hashtag. There's one line comment in the previous python file. We typically use line comments to describe complex features or to remind us to come back and change code later.

```
    # We convert age to an int before we multiply it by 10.
```

Code Blocks
===========

Python is an indented language. What this means is that sections of code that we run begin and end with an indentation. Python code blocks are typically indented with 4 spaces. Blocks of code can be found in functions, classes, if, while and for loops.
Consider this code.

```
    print("I'm out of a code block")
    if True:
        print("I'm in a block")
        number = 4
        print(number * 3)
    print("I'm out of a code block")
```

There is a code block after the if statement.if Statement

Use the if statement and a comparison to decide what code blocks should run.

```
    if True:
        some_number = 2
        print('this code ran', some_number)

    if False:
        another_number = 4
        print('did this code run?', another_number)

    some_number = 2
    if some_number <= 2:
        another_number = some_number * 4
        print('this code ran', another_number)
```

The code block beneath an if statement will execute if the comparison is True. Use the else statement if you would like to offer an alternative code block that executes when the coparison is False.
To check if some_number is above a certain value you could do something like this.

```
    some_number = 3
    if some_number > 4:
        print('some_number is greater than 4')

    if some_number <= 4:
        print('some_number is less than or equal to 4')
```

But this would be easier to read and less likely to introduce an error. only one of the code blocks in this statement will run.

```
    some_number = 3
    if some_number > 4:
        print('some_number is greater than 4')
    else:
        print('some_number is less than or equal to 4')
```

The elif else if statement will let you chain together comparisons. Again this makes your code easier to understand and ensures that only one of the code blocks runs.

```
    some_number = 3
    if some_number > 4:
        print('some_number is greater than 4')
    if 2 > some_number <= 4:
        print('some_number is greater than 2 and less than or equal to 4')
    if some_number > 0:
        print('some_number is greater than 0')
    else:
        print('some_number is less than or equal to 0')
```

while Loop
==========

If you need repeatedly run a code block use a loop. Like the if statement the while loop uses a comparison. If the comparison is True the code block will continue to run.

```
    some_number = 0
    while some_number < 100:
        some_number = some_number + 10
        print('some_number is less than 100', some_number)
    print('some_number is now', some_number)
```

for Loop
========

Another type of loop is the for loop. The for loop does not use a comparison like the while loop. The for loop is useful when you would like to use a counter in your code block. Also useful if you would like to pull individual values from a list or collection into your code block. This is called iteration.
You can use the range() function to count numbers.

```
    sum = 0
    for number in range(10):
        sum = sum + number
        print('number',number,'sum',sum)

    number 0 sum 0
    number 1 sum 1
    number 2 sum 3
    number 3 sum 6
    number 4 sum 10
    number 5 sum 15
    number 6 sum 21
    number 7 sum 28
    number 8 sum 36
    number 9 sum 45
```

For loops can walk through a list.

```
    names = ['Steve', 'Ned', 'Klaus', 'Jane']
    for name in names:
        if name == 'Klaus':
            print('Bye',name)
        else:
            print('Hi',name)

    Hi Steve
    Hi Ned
    Bye Klaus
    Hi Jane
```

Define a function
=================

Functions are sections of code that we can reuse throughout our program. Functions usually are defined to do one thing really well. One function that you've used in the previous lessons is the print() function. Print does one thing really well, it pushes data to the screen. Another function we've used previously is range(). This function generates numbers for us that we can loop through.
Range() and print() are examples of system functions. System functions are functions that are available to you in Python. Functions that you create are called user defined functions. You might create a function to calculate the sum of two numbers or to create a greeting. These are special custom functions that you create.
Similar to variables, all functions must have a name. The first line of a function is where we name the function. The def keyword is used to identify the name of a function. It comes before the name. Parentheses come after the name of the function. The code that makes up a function is in an indented block below this line. For example:

```
    def say_hello():
        print('Hello')
```

To run or call a function just type the name and the parantheses.

```
    >>> def hello():
    ...     name = input('Name? ')
    ...     print('Hello', name)
    ...
    >>> hello()
    Name? Jack
    Hello Jack
    >>>
```

Use parameters
==============

Parameters are values that you pass into a function from outside a function. You've done this previously with the print() and range() functions. To add parameters to your user defined function add variable names within the parantheses that come after the function name. These variables will be available within the code block of your function.

```
    >>> def hello(name):
    ...     print('Hello',name)
    ...
    >>> hello('John')
    Hello John

    >>> def to_third_power(num):
    ...     print(num**3)
    ...
    >>> to_third_power(2)
    8
```

You may define functions with multiple parameters.

```
    >>> def power(num, pow):
    ...     print(num**pow)
    ...
    >>> power(2, 3)
    8Return results
```

Functions may return results. These results can be displayed on the screen or used in other calculations.

```
    >>> def power(num, pow):
    ...     return num**pow
    ...
    >>> power(2, 3)
    8
    >>> 4 + power(2,3)
    12
    >>> print('power 2**3 =', power(2, 3))
    power 2**3 = 8
```

In Python functions may return multiple values.

```
    >>> def hello(name, age):
    ...     greeting = 'Hello' + name
    ...     in_ten_years = age + 10
    ...     return greeting, in_ten_years
    >>> g,t = hello('John', 10)
    >>> print(g, t)
    Hello John 20
```

