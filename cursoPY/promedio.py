def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    :param numbers: List of numbers integer or float
    :type numbers: list
    :return: Average of the numbers
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Example usage
print(calculate_average([1, 2, 3, 4, 5]))