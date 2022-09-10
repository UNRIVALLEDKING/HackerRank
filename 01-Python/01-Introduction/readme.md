<h1 align="center">Python Introduction Notes 🚀</h1>

## Python Print Function

This will print everything inside Quotation marks "......" .

```bash
print("Hello World!")
```

We can also use single quote instead of double like here.

```bash
print('Hello World!')
```

### printing something using variables.

let's assume there is a variable (variables are container that stores a value).
this_string = "Hello World!"

here this_string is the variable that store "Hello World!" we can store anything in that sring instead of "Hello World!".

here are some examples what we can store in a variable.

```bash
new_string = "This is UNRIVALLEDKING'S Repo."
my_string = "What do you want to store in this variable?"
my_string = "Hello, I'm back using same variable name twice in a same file. this will overwrite the previous value of this_string."
```

as we can see here we can name the string anything we want and use it to store any value we want.

### let's print these variables

```bash
print(this_string)
print(new_string)
print(my_string)
```

this will print all those values that we have stored in those variables. as we can see here that we didn't used any Quotation mark here 'cause we are using variables and calling that variable inside the print function.

## Python If Else

```bash
a = 18
b = int(input("What's your age? "))

if b >= a:
    print("You are an adult")
else:
    print("Your aren't an adult")
```

Here we are taking an input and converting it into integer {int() converts the number into an integer}.
then telling the program that if the number received is greater than a i.e, 18 then print that the the user is an adult.
else in all other cases he is a child not an adult.

## Elif, AND & OR

```bash
x = 20
teen = 13

age = int(input("What's your age? "))

if age >= teen and age < x:
    print("You're a Teenager.")
elif age >= x:
    print("You're an adult.")
else:
    print("You're a child.")
```

We can also write the above program as this. this method is without using AND

```bash
if teen <= age < x:
    print("You're a Teenager.")
elif age >= x:
    print("You're an adult.")
else:
    print("You're a child.")
```

# <----------------- Part 1 Over ----------------->

## Arithmetic Operators

These operators are used for performing arithmetical operations.
let's assume two numbers.

```bash
a = 12
b = 3
```

### Addition

```bash
print(a+b)
```

### Subtraction

```bash
print(a-b)
```

### Multiplication

```bash
print(a*b)
```

### Division

```bash
print(a/b)
```

### Exponent

```bash
print(a**n) # where n is exponential number like

print(a**2)
print(a**3)
```

### Remainder

```bash
print(a%b)
```

# <----------------- Part 2 Over ----------------->

## Type Conversion

Sometimes it's necessary to perform conversions between the built-in types. To convert between types you simply use the type name as a function. In addition, several built-in functions are supplied to perform special kinds of conversions. All of these functions return a new object representing the converted value.

```bash
x = "12"

# Here x is string. using type() function will return the type of the data.

print(type(x))

# now convert it to different data types.

x = int(x) # This will convert x into an interger
print(type(x)) # to print the dataType of the variable.
x = float(x) # This will convert x into an interger
print(type(x)) # to print the dataType of the variable.

```

## Loops

Python has two loop commands

- While Loop
- For Loop

<h3 align="center">While Loop 🔃</h3>
<hr/>
while loop executes a set of statements as long as a condition is true.

```bash
i = 1
while i < 10:
    print(i)
    i += 1 # remember to increment i, or else the loop will continue forever
```

<h3 align="center">For Loop 🔃</h3>
<hr/>
For loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). with the

`for` loop we can execute a set of statements, once for each item in a list, tuples, set, etc.

- Looping through set/tuple/list.

```bash
fruits = ["apple", "mango", "orange", "pineapple",
          "strawberry", "watermelon", "banana", "cherry"]

for i in fruits:
    print(i)
```

- Looping through a String.

```bash
for i in "Hello World!":
    print(i)
```

## Break Statment

`break` statement can stop the loop before it has looped through all the items.

```bash
fruits = ["apple", "mango", "orange", "pineapple",
          "strawberry", "watermelon", "banana", "cherry"]

for i in fruits:
    if i == "strawberry":
        break
    print(i)
```

## Continue Statement

`continue` statement can stop the current iteration of the loop and continue with the next ones.

```bash
fruits = ["apple", "mango", "orange", "pineapple",
          "strawberry", "watermelon", "banana", "cherry"]

for i in fruits:
    if i == "strawberry":
        continue
    print(i)
```

<hr/>

<h2 align="center">The range() Function</h2>

The `range()` function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

Note : we can change the defaults according to our need.

```bash
for i in range(10):
    print(i)
# range(10) is not the values of 0 to 10, but the values 0 to 9
```

- Changing the default starting point

```bash
for i in range(3,10):
    print(i)
# range(3,10) which means values from 3 to 10 (but not including 10).
```

- Changing the default increment sequence

```bash
for i in range(4,10, 2):
    print(i)
# range(4,10,2) the third parameter here i.e, 2 is the increment value.
```

first parameter is starting value, second parameter is ending value (excluding the number itself) & the third one is increment value we can use this pattern to set up a list according to our need.

<hr/>
<h2 align="center">Write a Function</h2>

A function is a block of code which only runs when it's called. we can pass data (paramenters) into a function.
it can also return data as a result.

- Creating a Funtion.

```bash
def my_function():
    print("Hello, this is my first function.")
```

- Calling a Function

```bash
def my_function():
    print("Hello, this is my first function.")

my_function()
```

## Here are some more examples.

```bash
def hello(name):
    print("Hello", name)

hello("UNRIVALLEDKING")
hello("Monkey D Luffy")
hello("Zoro")
hello("Harry")
```

# <---------------------- Python Introduction Over ---------------------->
