# Write a Python program to multiply all the items in a list.

def multiply_list(a_list):
    value = 1
    for item in a_list:
        value = value * item
        pass
    return value
    pass

print(multiply_list([3, 4, 5]))