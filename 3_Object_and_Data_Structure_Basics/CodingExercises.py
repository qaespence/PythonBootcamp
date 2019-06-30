# <summary>
# Udemy course - Python Bootcamp: Section 3: Object and Data Structure Basics
# </summary>

# Coding Exercise 1: Numbers: Simple Arithmetic
# Write an expression that equals 100
80 + 20

# Coding Exercise 2: Quick Print Check
# print out the phrase "Hello World"
print("Hello World")

# Coding Exercise 3: String Indexing
# Write a string index that returns the letter 'r' from 'Hello World'
'Hello World'[8]

# Coding Exercise 4: String Slicing
# Use string slicing to grab the word 'ink' from inside 'tinker'
'tinker'[1:4]

# Coding Exercise 5: Print Formatting
# Write an expression using string formatting to return the phrase 'Python rules!'
'{0} {1}!'.format('Python', 'rules')

# Coding Exercise 6: Lists
# Create a list that contains at least one string, one integer, and one float
['a string', 7, 3.14]

# Coding Exercise 7: Dictionaries
# Create a dictionary where all the keys are strings and all the values are integers
{'test1':10, "test2":25, "test3":5}

# Coding Exercise 8: Sets
# Write an expression that would turn the string 'Mississippi' into a set of unique letters
set('Mississippi')

# Coding Exercise 9: File I/O
# Write a script that opens a file named 'test.txt', writes 'Hello World' to Arithmetic
# file, and the closes it
x = open('test.txt', mode='w')
x.write('Hello World')
x.close()
