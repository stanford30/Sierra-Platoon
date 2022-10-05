array_to_search_through = []
for number in range(1, 1001):
    array_to_search_through.append(number)


def linear_search(value_to_find, array_to_search_through: list):
    # init value
    found_value = None
    # if value_to_find is in array_to_search_through
    if value_to_find in array_to_search_through:
        #set found value to index
        found_value = array_to_search_through.index(value_to_find)
    #return found value, None if not in array.
    return found_value


def linear_search_global(value_to_find, array_to_search_through):
    #init python list
    arr = []
    #enumerate through array_to_search_through for index(i) and element(x)
    for i, x in enumerate(array_to_search_through):
        #if element(x) == value_to_find append it to arr(list)
        if x == value_to_find:
            arr.append(i)
    #return arr with indices
    return arr