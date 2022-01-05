def binary_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    complexity: O(log n)
    """
    first = 0
    last = len(list) - 1
    
    while(first <= last):
        midpoint = (first+last)//2
        if list[midpoint] == target:
            return midpoint
        if list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None

# provide sorted list
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = -1

print("Target at index: ", binary_search(numbers, target))
