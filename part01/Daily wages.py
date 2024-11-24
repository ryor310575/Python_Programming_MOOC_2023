# Please write a program which asks for the hourly wage, hours worked, and the day of the week.
# The program should then print out the daily wages, which equal hourly wage multiplied by hours worked,
# except on Sundays when the hourly wage is doubled.
#
# Sample output
# Hourly wage: 8.5
# Hours worked: 3
# Day of the week: Monday
# Daily wages: 25.5 euros
#
# Sample output
# Hourly wage: 12.5
# Hours worked: 10
# Day of the week: Sunday
# Daily wages: 250.0 euros
h_wage=float(input("Hourly wage: "))
h_worked=float(input("Hours worked: "))
d_week=input("Day of the week: ")
d_wage=h_wage*h_worked
if d_week=="Sunday":
    d_wage=d_wage*2
print(f"Daily wages: {d_wage} euros")