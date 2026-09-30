
# tuple swap
a = 1
b = 2
a, b =  b, a

arr1 = [1, 3, 7]
arr2 = [4, 5]

# index + value 
for i, val in enumerate(arr1):
    print(i, val)

# parallel iteration
for a, b in zip(arr1, arr2):
    print(a, b)
    
# ternary operator
# c# var max = a > b ? a : b;
x = a if a > b else b

# string operators
chars = ['a', 'b', 'c']
s = "a sentence split, by comma"
"".join(chars)
words = s.split(",")


# binay search
import bisect
i = bisect.bisect_left(arr1, 2) # leftmost insetion point
i2 = bisect.bisect_right(arr1, 2) # rightmost insertion points


# pythonic patterns
if any(x > 5 for x in arr1):
    print("at least one element is greater than 5")
if all(x > 3 for x in arr1):
    print("all elements are greater than 0")
    
longest = max(words, key=len)

# flattening
flat = [x for sublist in [[1, 2], [3, 4], [5]] for x in sublist]
print(flat)
