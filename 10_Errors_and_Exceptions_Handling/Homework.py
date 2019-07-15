
# Udemy course - Complete Python Bootcamp
# Section 10 Homework Assignment


# Problem 1
# Handle the exception thrown by the given code

try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("Why are you doing math on characters?")

# Problem 2
# Handle the exception thrown by the given code
# Use a finally block to print 'All Done.'

try:
    x = 5
    y = 0
    z = x/y
except:
    print("Oops, can't divide by zero!")
finally:
    print("All Done.")

# Problem 3
# Write a function that asked for an integer and prints the square of it
# Use a while loop with a try, except, else block to account for incorrect inputs

def ask():
    while True:
        try:
            data = int(input("Please enter an integer and I'll square it: "))
        except:
            print("Are you sure that was a number?")
            continue
        else:
            break
    print("The square is: " + str(data**2))

ask()
