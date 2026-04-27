# pyhton hashset implementation using built-in set data structure

"""
c# comparision:
HashSet<int> seen = new HashSet<int>();
seen.Add(5);
if (seen.Contains(5))
seen.Remove(5);
setA.IntersectWith(setB);
setA.UnionWith(setB);
"""

seen = set()
seen.add(5)

if 5 in seen:
    seen.remove(5)

seen.discard(5) # discard does not raise an error if the element is not present

print(seen) # Output: set()

a = set([1, 2, 3])
b = set([3, 4, 5])

print (a.union(b)) # Output: {1, 2, 3, 4, 5}
print (a.intersection(b)) # Output: {3}
print (a.difference(b)) # Output: {1, 2}

print (a & b) # Output: {3} (intersection)
print (a | b) # Output: {1, 2, 3, 4, 5} (union)
print (a - b) # Output: {1, 2} (difference)