#
# Shane Bishop
# 101030053
#
# Reference List:
# Gaddis, T. (2015). "Starting Out With Python"
# Mathematical functions. (2016-09-27). Retrieved from https://docs.python.org/3/library/math.html.
#

import math # Import the math module

# Ask the user for the lengths of the arms of the right angle triangle
length_of_first_arm  = int(input(" What is the length of the first side? "))
length_of_second_arm = int(input("What is the length of the second side? "))

# Calculate the length of the hypotenuse, and the diameter, circumference, and area of the circle
hypotenuse    = (length_of_first_arm ** 2 + length_of_second_arm ** 2) ** 0.5
diameter      = 2 * hypotenuse
circumference = 2 * math.pi * hypotenuse
area          = math.pi * hypotenuse ** 2

# Print the calculated values
print("The length of the hypotenuse/radius is", hypotenuse, "units.")
print("The diameter is", diameter, "units.")
print("The circumference is", circumference, "units.")
print("The area is", area, "units squared.")