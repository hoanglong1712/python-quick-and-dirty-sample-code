#  Write a Python program to find the smallest number in a list.

def smallest_value_in_list(a_list):
    if a_list is None or len(a_list) == 0:
        return None
        pass
    smallest = a_list[0]
    for item in a_list:
        if smallest > item:
            smallest = item
            pass
        pass
    return smallest
    pass

print(smallest_value_in_list([1, -20, -8, 0]))