def divisible(numerator: int, denominator: int) -> bool:
    """
    Check if the numerator is divisible by the denominator without a remainder.
    """
    return numerator % denominator == 0

# Example usage giving Fasle answer because 30 is not divisable by 4 without a remainder
# print(divisible(30, 4))

# Example usage giving True answer because 30 is divisable by 3 without a remainder
print(divisible(30, 3))