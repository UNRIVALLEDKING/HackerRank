<h1 align="center">Python Basic Data Types 🚀</h1>

## Lists

Python Lists are just like dynamically sized arrays, declared in other languages (vector in C++ and ArrayList in Java). In simple language, a list is a collection of things, enclosed in [ ] and separated by commas.

```bash
fruits = ["apple", "mango", "strawberry"]
print(fruits)
```

## List Comprehension

List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

### Without List Comprehension

```bash
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
filterFruits = []

for i in fruits:
  if "a" in 1:
    filterFruits.append(i)

print(filterFruits)
```

### With List Comprehension

```bash
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

filterFruits = [x for x in fruits if "a" in x]

print(filterFruits)
```

## Sort Function

Sorting list in ascending/descending order.

```bash
numbers = [3,55,64,2,4,6,2,4,676,432,64]
print("Without Sorting",numbers)
numbers = numbers.sort()
print("After Sorting",numbers)
```

# <-------------------- Python Basic Data Types Over -------------------->
