def has_even(numbers):
    """
    Search for an even number in a list.

    Returns:
    - True if an even number is found.
    - False if no even number is found.
    """
    for number in numbers:
        if number % 2 == 0:
            return True
    return False

# usage
numbers_list = [1, 3, 5, 7, 8, 9]
result = has_even(numbers_list)
print(result)

#A lambda function to calculate the volume of a cylinder
calculate_cylinder_volume = lambda radius, height: 3.14159 * radius ** 2 * height

# usage
radius = 2
height = 5
volume = calculate_cylinder_volume(radius, height)
print(volume)
