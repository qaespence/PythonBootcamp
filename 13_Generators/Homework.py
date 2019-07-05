# <summary>
# Udemy course - Complete Python Bootcamp
# Section 13 Homework Assignment
# </summary>

# Problem 1
# Create a generator that generates the squares of numbers up to some number N
def gensquares(n):
    for i in range(n):
        yield n**2


# Problem 2
# Create a generator that yields "n" random numbers between a low and a high number
import random

def rand_num(low,high,n):
    for num in range(n):
        yield random.randint(low,high)


# Problem 3
# Use the iter() function to convert a string into an iterator
s = "hello"
s = iter(s)
print(next(s))
