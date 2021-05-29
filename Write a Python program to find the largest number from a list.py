# Write a Python program to find the largest number from a list.

def max_value_in_list(a_list) -> object:
    if a_list is None or len(a_list) == 0:
        return None
        pass 
    max_value = a_list[0]
    for item in a_list:
        if max_value < item:
            max_value = item
            pass
        pass 
    return max_value
    pass

print(max_value_in_list([1, -3, -8, 0]))