# Please write a program which asks the user for a temperature in degrees Fahrenheit, and then prints out the same in degrees Celsius.
# If the converted temperature falls below zero degrees Celsius, the program should also print out "Brr! It's cold in here!".
# The formula for converting degrees Fahrenheit to degrees Celsius can be found easily by any search engine of your choice.

# To convert a temperature from Fahrenheit to Celsius, you can use the following formula:
# °C = (°F - 32) × 5/9
# Two examples of expected behaviour:
#
# Sample output
# Please type in a temperature (F): 101
# 101 degrees Fahrenheit equals 38.333333333333336 degrees Celsius
#
# Please type in a temperature (F): 21
# 21 degrees Fahrenheit equals -6.111111111111111 degrees Celsius
# Brr! It's cold in here!
farenheit=int(input("Please type in a temperature (F): "))
celcius=0.0
celcius=(farenheit-32)*5/9
print(f"{farenheit} degrees Fahrenheit equals {celcius} degrees Celsius")
if celcius<0:
    print("Brr! It's cold in here!")