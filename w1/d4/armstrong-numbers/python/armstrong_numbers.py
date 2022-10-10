# How can you make this more scalable and reusable later?
import functools


def find_armstrong_numbers(numbers):
    # ans = []
    # for number in numbers:
    #     number = str(number)
    #     sum = 0
    #     length = len(number)
    #     for a in number:
    #         sum += int(a)**length
    #     if sum == int(number):
    #         ans.append(sum)

    # return ans
    # numbers = [str(x) for x in numbers]
    ans = []
    for x in numbers:
        if helper(x) == x:
            ans.append(x)
    return ans


def helper(num):
    digits = [int(x) for x in str(num)]
    length = len(digits)
    sum = functools.reduce(lambda agg, d: agg + (d**length), digits, 0)
    return sum


# helper(371)
# helper(5)