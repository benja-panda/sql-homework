
def reverse_tuple(tup):
    """Reverses the order of items in a tuple.

    :param tup: The original tuple to reverse
    :return: A new tuple containing the items in reverse order
    """
    result = []
    for i in range(len(tup) - 1, -1, -1):
        result.append(tup[i])
    return tuple(result)


print(reverse_tuple((1, 2, 3, 4)))
print(reverse_tuple(("a", "b", "c")))
print(reverse_tuple(()))

######


import random


def random_tuple(length):
    """Generates a tuple of random integers between 1 and 100.

    :param length: The number of random integers to include
    :return: A tuple of 'length' random integers
    """
    result = []
    for _ in range(length):
        result.append(random.randint(1, 100))
    return tuple(result)


print(random_tuple(5))
print(random_tuple(3))
print(len(random_tuple(10)))

#######

def flat_dict(d):
    """Flattens a dictionary into a tuple of alternating keys and values.

    :param d: The dictionary to flatten
    :return: A tuple containing all keys followed by their corresponding values
    """
    result = []
    for key in d:
        result.append(key)
        result.append(d[key])
    return tuple(result)


# Function calls
print(flat_dict({"a": 1, "b": 2, "c": 3}))
print(flat_dict({"name": "dana", "age": 29}))
print(flat_dict({}))