# Please write a program which asks for the names and ages of two persons.
# The program should then print out the name of the elder.
#
# Some examples of expected behaviour:
#
# Sample output
# Person 1:
# Name: Alan
# Age: 26
# Person 2:
# Name: Ada
# Age: 27
# The elder is Ada
#
# Sample output
# Person 1:
# Name: Bill
# Age: 1
# Person 2:
# Name: Jean
# Age: 1
# Bill and Jean are the same age
print("Person 1:")
person_1_name=input("Name: ")
person_1_age=int(input("Age: "))
print("Person 2:")
person_2_name=input("Name: ")
person_2_age=int(input("Age: "))
if person_1_age>person_2_age:
    print(f"The elder is {person_1_name}")
elif person_2_age>person_1_age:
    print(f"The elder is {person_2_name}")
else:
    print(f"{person_1_name} and {person_2_name} are the same age")