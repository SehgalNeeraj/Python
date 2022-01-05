def binary_search_recursive(list, target):
    """
    Returns the index position of the target if found, else returns None
    complexity: O(log n)
    """
    if len(list) <= 0:
        return None

    midpoint = len(list)//2
    if list[midpoint] == target:
        return True
    if list[midpoint] < target:
        return binary_search_recursive(list[midpoint + 1:], target)
    else:
        return binary_search_recursive(list[:midpoint], target)

# provide sorted list
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 11

print("Target at index: ", binary_search_recursive(numbers, target))
