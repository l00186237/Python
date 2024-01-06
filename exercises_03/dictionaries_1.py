# Creating a dictionary
my_dict = {
    'name': 'John',
    'age': 40,
    'city': 'Sligo',
    'occupation': 'Software Engineer'
}

# Accessing values in the dictionary
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])
print("City:", my_dict['city'])
print("Occupation:", my_dict['occupation'])

# Modifying values in the dictionary
my_dict['age'] = 26
my_dict['city'] = 'Dublin'

# Adding a new key-value pair
my_dict['language'] = 'Python'

# Displaying the updated dictionary
print("\nUpdated Dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Removing a key-value pair
del my_dict['occupation']

# Displaying the dictionary after removing a key-value pair
print("\nDictionary after removing 'occupation':", my_dict)
