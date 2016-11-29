#
# Shane Bishop
# 101030053
#
# Reference List:
# Gaddis, T. (2015). "Starting Out With Python"
#

# Ask the user for a word to convert into "Uppercase Pig Latin"
input = input("What is the word? ")

# Perform the conversion
output = input[1:] + input[0] + "ay"
output = output.upper()

# Output the word in "Uppercase Pig Latin"
print("In Pig Latin, that word is:", output)