# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the largest number in a given array.

def find_max(l):
    max = l[0]
    for i in l:
        if i > max:
            max = i
    return max

# print(find_max([1, 4, 45, 6, -50, 10, 2]))
# => 45