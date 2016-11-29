#
# Shane Bishop
# 101030053
#
# Reference List:
# Gaddis, T. (2015). "Starting Out With Python"
#

# Ask the user for a number of days
num_days = int(input("How many days? "))

# Calculate the number of years and subtract the days accounted for from the number of days
num_years  = num_days // 365
num_days   = num_days - num_years  * 365

# Calculate the number of months and subtract the days accounted for from the number of days
num_months = num_days // 30
num_days   = num_days - num_months * 30

# Calculate the number of weeks and subtract the days account for from the number of days
num_weeks  = num_days // 7
num_days   = num_days - num_weeks  * 7

# Print the number of years, months, weeks, and days
print(num_days, "days is", num_years, "year(s),", num_months, \
	"month(s)", num_weeks, "week(s), and", num_days, "days.")