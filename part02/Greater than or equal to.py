# Please write a program which asks for two integer numbers.
# The program should then print out whichever is greater.
# If the numbers are equal, the program should print a different message.
#
# Some examples of expected behaviour:
#
# Sample output
# Please type in the first number: 5
# Please type in another number: 3
# The greater number was: 5
#
# Sample output
# Please type in the first number: 5
# Please type in another number: 8
# The greater number was: 8
#
# Sample output
# Please type in the first number: 5
# Please type in another number: 5
# The numbers are equal!
num_1=int(input("Please type in the first number: "))
num_2=int(input("Please type in another number: "))
if num_1>num_2:
    print(f"The greater number was: {num_1}")
elif num_2>num_1:
    print(f"The greater number was: {num_2}")
else:
    print("The numbers are equal!")