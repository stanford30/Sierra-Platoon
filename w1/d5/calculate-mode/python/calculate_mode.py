from collections import Counter


def calculate_mode(l):
    print(Counter(l).most_common())


calculate_mode([1, 2, 3, 3])  # => [3]
calculate_mode([4.5, 0, 0])  # => [0]
calculate_mode([1.5, -1, 1, 1.5])  # => [1.5]
calculate_mode([1, 1, 2, 2])  # => [1,2]
calculate_mode([1, 2, 3])  # => [1,2,3], because all occur with equal frequency
calculate_mode(["who", "what", "where", "who"])  # => ["who"]
