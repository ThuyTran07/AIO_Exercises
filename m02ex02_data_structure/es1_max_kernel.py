### ESSAY 1 ###
# find max in k-size list sliding window
# Step 1 - find position of sliding window
# Step 2 - slice the list
# Step 3 - append into result list


def max_kernel(num_list, k):
    max_list = []
    for i in range(len(num_list) - k + 1):
        sub_list = num_list[i:i+k]
        max_list.append(max(sub_list))
    return max_list


# MC1
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(f"MC1: {max_kernel(num_list, k)} - Answer: a)")
