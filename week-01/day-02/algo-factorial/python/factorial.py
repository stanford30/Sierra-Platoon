def factorial(num):
    # your code here
    if num == 0 or num == 1:
        return 1

    return num * factorial(num - 1)
