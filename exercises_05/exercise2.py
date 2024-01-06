def find_num(number_list: list, number: int) -> bool:
    """
    Check if the specified number is in the list.
    """
    for iterate_number in number_list:
        if iterate_number == number:
            return True
        else:
            pass

# Example usage
result = find_num([1, 2, 3, 4, 5, 6, 7, 8], 9)
print(result)


###modified function to return false

def find_num(number_list: list, number: int) -> bool:
    """
    Check if the specified number is in the list.
    """
    for iterate_number in number_list:
        if iterate_number == number:
            return True
        else:
            return False

# Example usage
result = find_num([1, 2, 3, 4, 5, 6, 7, 8], 9)
print(result)

