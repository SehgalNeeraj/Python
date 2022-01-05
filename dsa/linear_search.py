# Implement Linear Search - search sequentially, incrementing step-wise
######################################################################
# 1. start at first value
# 2. Increment step if not found
# 3. Say "Not found" if value not found after iterating till end bound

# Runtime: O(n)
######################################################################
def linear_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    
    return None

numbers = [0,1,2,3,4,5,10,9,8,7,6]
target = 6

print("Target at index: ", linear_search(list,target))