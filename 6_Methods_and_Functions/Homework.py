# <summary>
# Udemy course - Complete Python Bootcamp
# Section 6 Homework Assignment
# </summary>

# Write a function that computes the volume of a sphere given its radius
def vol(rad):
    return (4.0/3)*(3.14159)*(rad**3)


# Write a function that checks whether a number is in a given range
# (Inclusive of high and low)
def ran_check(num,low,high):
    if num in range(low,high+1):
        print f'The number {num} is between {low} and {high}.'
    else:
        print f'The number {num} is outside the range of {low} and {high}.'


def ran_bool(num,low,high):
    return num in range(low,high+1)


# Write a Python function that accepts a string and calculate the number
# of upper case letters and lower case letters
def up_low(s):
    lower_chars = 0
    upper_chars = 0
    for char in s:
        if char != ' ' and char.isupper():
            upper_chars += 1
        if char != ' ' and char.islower():
            lower_chars += 1
    print f'Original String : {s}'
    print f'No. of Upper case characters : {upper_chars}'
    print f'No. of Lower case characters : {lower_chars}'


# Write a Python function thay takes a list and returns a new list with
# unique elements of the first list
def unique_list(l):
    unique_list = []
    for num in l:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list


# Write a Python function to multiple all the numbers in a list
def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


# Write a Python function that checks whether a passed string is a
# palindrome or not
def palindrome(s):
    words = s.split()
    combined = "".join(words).lower()
    return combined == combined[::-1]


# Write a Python function to check whether a string is a pangram or not
import string
def ispangram(str, alphebet=string.ascii_lowercase):
    for char in str:
        if char in alphebet:
            alphebet.replace(char,"")
    return len(alphebet) == 0

def ispangram2(str, alphebet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str.lower())
