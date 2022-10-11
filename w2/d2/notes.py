from datetime import datetime


def AddOne(num):
    return num + 1


def MultiplyByTwo(num):
    return num * 2


# This function accepts a function as input, then returns a new function that
# behaves similarly to the one that is passed in
def PrintCurrentTimeAndAlso(func):

    # this function accepts any number of positional arguments (*args) and any
    # number of named arguments (**kwargs)
    def WrapperFunction(*args, **kwargs):
        print(f'Calling {func.__name__} at {datetime.now()}')
        return func(*args, **kwargs)

    return WrapperFunction


# This creates a new, decorated function
PrintCurrentTimeAndAlsoAddOne = PrintCurrentTimeAndAlso(AddOne)
one_plus_one = PrintCurrentTimeAndAlsoAddOne(1)

# This creates a new, decorated function
PrintCurrentTimeAndAlsoMultiplyByTwo = PrintCurrentTimeAndAlso(MultiplyByTwo)
two_times_two = PrintCurrentTimeAndAlsoMultiplyByTwo(2)

# Using the decorator syntax (@) allows us to create a decorated function all
# at once,

# instead of creating an undecorated function, and then passing it into the
# decorator


@PrintCurrentTimeAndAlso
def SubtractThree(num):
    return num - 3


# nine_minus_three = SubtractThree(9)
print(SubtractThree(9))
