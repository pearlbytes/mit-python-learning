# MIT 6.0001 Problem Set 0 
# This program reads two numbers from the user, calculates x**y, 
# and prints the log base 2 of x

import math # Import math library to use log2
# Ask the user for input
x = float(input("Enter number x: "))  # convert input to number
y = float(input("Enter number y: "))
# Compute x raised to the power y
power = x ** y
print("X**y =", power)

# Compute log base 2 of x
log_x = math.log2(x)
print("log(x) =", log_x)