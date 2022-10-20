sequence = [4, 3, 5, 0, 1, 0, 0, 0, 10, 0, 2, 1, 3, 4, 5]
swaps = 0

# Your Code Here
prev = 0
curr = 1
while curr < len(sequence):
    prev_num = sequence[prev]
    curr_num = sequence[curr]
    if curr_num < prev_num:
        sequence[prev] = curr_num
        sequence[curr] = prev_num
        swaps += 1
        if prev != 0:
            prev -= 1
            curr -= 1
    elif curr_num >= prev_num:
        curr += 1
        prev += 1

print(f"Final result: {sequence}")
print(f"Swaps: {swaps}")
