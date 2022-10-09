def sum_pairs(array, target):
    array.sort()
    ans = []
    i = 0
    j = len(array) - 1
    while (i < j):
        sum = array[i] + array[j]
        if sum == target:
            ans.append([array[i], array[j]])
            i += 1
        elif sum < target:
            i += 1
        else:
            j -= 1
    return ans
