import re


def palindrome(word):
    word = str(word).lower()
    # word.replace(r'-\s', '')
    # print(word)
    # pattern = '\s*-*,*\.*'
    pattern2 = '\W'
    replace = ''
    word = re.sub(pattern2, replace, word)
    print(word)
    return word == word[::-1]
