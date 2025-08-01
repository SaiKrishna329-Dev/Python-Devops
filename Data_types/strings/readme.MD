# Session 69

## Topics covered

- String datatype
  - Indexing and slicing
  - Properties
  - Methods
  - Print Formatting
- List datatype
  - Indexing and slicing
  - Methods
  - Properties

## String methods

- `len()` - Using this you can calculate the length of a string
- `upper()`
- `lower()`
- `capitalize()`
- `count()` - Count the occurrence of a word inside a given string
- `split()` - Split the string based on the character specified
- `splitlines()` - Spilt the given string based on new line character

## Indexing and Slicing

### Indexing

- In python, the indexing of an element starts from 0
- We specify the index of an element inside `[]`
- Python supports both +ve and -ve indexing i.e. 0, 1 and -1, -2

### Slicing

- The end index in the operation is not included in the result
- Therefore, we should only use **end-1** i.e `[start:end-1]`
- If the starting index is omitted, python considers it to be 0
- Similary, if the end index is not included, python will print it until the end of the string
- We can use step size to fetch elements at a specifed interval ie. `[start:end:step]`
  - If the step value is not specified, then python considers its value to be 1
  - For e.g. to reverse a string, we use: `[::-1]`

## Properties

- String are immutable i.e. the elements that are once defined cant be altered
- String concatenation (+)
- String multiplication (*)

## Print Formatting

- `.format()`

## List datatype

### Methods

- `append()` - Using append, you can only add one element at the end of a given list
- `extend()` - Using extend, you can only add more than one element at the end of a given list
  - Both append and extend methods are inplace operations i.e. they modify the original list
- `pop()` - To pop off an item from the list at a given index and is an inplace operation
- `reverse()` - Reverse a given list
- `sort()` - Sort a given a list and is an inplace operation
- `sorted()` - Sort and a return the sorted list

### Nesting Lists

- A list inside a list is called as nesting lists

### Unpacking

- Extract individual values from a list into its individual variables

### Properties of List

- List is a mutable datatype i.e. the elements can be altered after they're defined
- It also supports '+', '*' i.e. extending original list