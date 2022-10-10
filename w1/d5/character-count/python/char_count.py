from collections import Counter


def char_count(str):
    # str = sorted(''.join(str.split(' ')))

    # my_dict = {}
    # for x in str:
    #     if x not in my_dict:
    #         my_dict[x] = 1
    #     else:
    #         my_dict[x] += 1

    # ans = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

    # # print([[i, v] for i, v in ans])

    # return [[i, v] for i, v in ans]
    # print(ans)
    holder = []
    str_sort = sorted(''.join(str.split(' ')))
    print(str_sort)
    count_dict = Counter(str_sort)
