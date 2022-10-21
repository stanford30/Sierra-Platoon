sequence = [4, 3, 5, 0, 1]
swaps = 0

# Your Code Here
# prev = 0
# curr = 1
# while curr < len(sequence):
#     prev_num = sequence[prev]
#     curr_num = sequence[curr]
#     if curr_num < prev_num:
#         sequence[prev] = curr_num
#         sequence[curr] = prev_num
#         swaps += 1
#         print(sequence)
#         if prev != 0:
#             prev -= 1
#             curr -= 1
#     elif curr_num >= prev_num:
#         curr += 1
#         prev += 1


swapped = True
while swapped:
    swapped = False
    for i in range(len(sequence) - 1):
        if sequence[i] > sequence[i + 1]:
            prev = sequence[i]
            sequence[i] = sequence[i + 1]
            sequence[i + 1] = prev
            swapped = True
            swaps += 1
        print(sequence)


print(f"Final result: {sequence}")
print(f"Swaps: {swaps}")
