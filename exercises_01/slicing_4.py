# Strings are immutable, that means you cannot change the string. 
# You can however slice the string and reassemble a new string with changes

a = "John"
first_letters = a[0:2:1]
last_letter = a[-1]
insert_letter = "a"
b = first_letters + insert_letter + last_letter
print(b)
