# Please write a program which asks the user for an integer number. If the number is less than zero,
# the program should print out the number multiplied by -1. Otherwise the program prints out the number as is.
# Please have a look at the examples of expected behaviour below.
#
# Sample output
# Please type in a number: -7
# The absolute value of this number is 7
#
# Sample output
# Please type in a number: 1
# The absolute value of this number is 1
#
# Sample output
# Please type in a number: -99
# The absolute value of this number is 99

num=int(input("Please type in a number:"))
abs_value=0
if num<0:
    abs_value=num*-1
else:
    abs_value=num
print(f"The absolute value of this number is {abs_value}")