# Variables
day = "Monday"
print(day)

# Concatenation
name = "Shau"
age = "2"
print ("Hello, " + name + " are you " + age + " years old?")

# Basic Arithmetics 
a = 12
b = 84
print(a * b)
print(a + b)
print(b / a)
print(b - a)

# Coding Challenge
import math

distance_of_A_to_B = input("What is the straight line distance, in 1miles, between point A to point B.")
in_kilometres = float(distance_of_A_to_B) * 1.6
flightpath = math.ceil((in_kilometres * 3.142)/2)
print("The distance between point A and point B along the flight path of the satalite is " + str(flightpath) + " kilometre.")

