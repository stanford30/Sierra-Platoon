# How can you make this more scalable and reusable later?
def find_armstrong_numbers(numbers):
    ans = []
    for number in numbers:
        number = str(number)
        sum = 0
        length = len(number)
        for a in number:
            sum += int(a)**length
        if sum == int(number):
            ans.append(sum)

    return ans
