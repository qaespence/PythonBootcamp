# <summary>
# Udemy course - Complete Python Bootcamp
# Section 6 Homework Assignment
# </summary>

# Write a function that computes the volume of a sphere given its radius
def vol(rad):
    return (4.0/3)*(3.14159)*(rad**3)

print(vol(2))


# Write a function that checks whether a number is in a given range
# (Inclusive of high and low)
def ran_check(num,low,high):
    if num in range(low,high+1):
        print(f'The number {num} is between {low} and {high}.')
    else:
        print(f'The number {num} is outside the range of {low} and {high}.')


def ran_bool(num,low,high):
    return num in range(low,high+1)

ran_check(3,1,10)
print(ran_bool(3,1,10))


# Write a Python function that accepts a string and calculate the number
# of upper case letters and lower case letters
def up_low(s):
    lower_chars = 0
    upper_chars = 0
    for char in s:
        if char.isupper():
            upper_chars += 1
        if char.islower():
            lower_chars += 1
    print(f'Original String : {s}')
    print(f'No. of Upper case characters : {upper_chars}')
    print(f'No. of Lower case characters : {lower_chars}')

up_low('Hello Mr. Rogers, how are you this fine Tuesday?')


# Write a Python function thay takes a list and returns a new list with
# unique elements of the first list
def unique_list(l):
    unique_list = []
    for num in l:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))


# Write a Python function to multiple all the numbers in a list
def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

print(multiply([1,2,3,-4]))


# Write a Python function that checks whether a passed string is a
# palindrome or not
def palindrome(s):
    words = s.split()
    combined = "".join(words).lower()
    return combined == combined[::-1]

print(palindrome('helleh'))


# Write a Python function to check whether a string is a pangram or not
import string
def ispangram(str, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str.lower())

print(ispangram("The quick brown fox jumps over the lazy dog"))
