
from collections import defaultdict
from collections import Counter


# dictionary for storing key-value pairs
map = {}

map["key"] = 1
map["key 2"] = 2
map["key 3"] = 3
map["key 4"] = 4


if "key" in map:
    val = map["key", 0]
    for k, v in map.items():
        print(k, v)

# dictionary of lists for representing a graph
graph = defaultdict(list)
graph["a"].append("b")

# frequency ma[p] for counting frequency of characters in a string
freq = defaultdict(int)
freq["x"] += 1

# Counter for counting frequency of characters in a string
s = "simple sentence frequecy"
freq = Counter(s)
freq.most_common(3)  # returns the 3 most common characters in the string
freq["z"] # returns 0 for characters not in the string


