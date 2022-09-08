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
