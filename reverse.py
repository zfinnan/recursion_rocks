# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# Write a recursive function called `reverse` that accepts a ss and returns a reversed ss.

def reverse(ss):
    rs = ''
    i = len(ss)
    while i > 0:
        rs += ss[i - 1]
        i = i - 1
    return rs

# print(reverse("")) 
# => ""
# print(reverse("a")) 
# => "a"
# print(reverse("ab")) 
# => "ba"
# print(reverse("computer")) 
# => "retupmoc"
# print(reverse(reverse("computer"))) 
# => "computer"