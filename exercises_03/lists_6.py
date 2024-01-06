# Defining a string containing comma-separated values
my_string = "12/9/22, 14:30, System start, UB2204-Server"

# Using the split() method to create a list of values by splitting the string at commas
list_of_values = my_string.split(",")

# Displaying the resulting list
print("List of values:", list_of_values)
