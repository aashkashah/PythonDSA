
# dictionary

# empty 
dict = {}

# set a value
dict["apple"] = 100

# get a value
val = dict["apple"]
val = dict.get("apple", 0)

# if exists
if "apple" in dict:
    pass

# key and values
for k, v in dict.items():
    print(v)
    
dict["apple"] = dict.get("apple", 0) + 1

# defaultdict, auto create missing keys
from collections import defaultdict

d = defaultdict(int)
d = defaultdict(list)
d["fruits"].append("mango")


# set
s = set()

# add and check
s.add(5)
if 5 in s:
    s.remove(5) # charses if mising
    s.discard(6) # silent if missing
    
# empty list
nums = []

nums = [0] * 5 

grid = [[0] * 3 for _ in range(3)] # 3x3 grid

nums.append(4)
nums.insert(0, 99) # O(n) operation, adds at index 0

nums.pop()
nums.pop(2)



