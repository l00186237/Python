# Defining a string with parentheses
text_with_brackets = "(John D was here)"

# Using strip() to remove leading and trailing parentheses
text_without_brackets = text_with_brackets.strip('(')
text_without_brackets = text_without_brackets.strip(')')

# Displaying the modified string
print(text_without_brackets)
