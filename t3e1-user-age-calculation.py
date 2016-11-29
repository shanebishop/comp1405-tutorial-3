#
# Shane Bishop
# 101030053
#
# Reference List:
# Gaddis, T. (2015). "Starting Out With Python"
#

# Ask the user for their name and the year they were born
username = input("What is your name? ")
year_born = int(input("Hello," + username + ", in what year were you born? "))

# Compute the user's current age
current_age = 2016 - year_born - 1

# Output the user's current age
print("You must be between", current_age, "and", current_age + 1, "years of age.")