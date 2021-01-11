# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the factorial of a given number.

def factorial(n):
    fact_nums = [x for x in range(1,n+1)]
    total = 1
    for num in fact_nums:
        total *= num
    return total

print(factorial(5))