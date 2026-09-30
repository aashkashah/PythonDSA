
'''
C# list and array comparision:
var list = new List<int>();
list.Add(1);
list.Sort();
list.Reverse();
list.Count;
list.removeAt(0);
'''

arr = [1, 2, 3]

# adding elements
arr.append(4) # adds an element to the end of the list
arr.insert(1, 2) # adds an element at a specific poisiton
arr.extend([5,6]) # adds multiple elements to the end of the list

# updating elements
arr[1] = 25 # updates element at index 1

# removing elements
arr.remove(25) # removes the first occurance of an element
arr.pop() # removes element at a specific index or last element if no index provided
arr.pop(0) # O(n) removes the first element of the list and shifts all other elements to the left
del arr[1] # deletes an element at a specific index 

arr.sort() # sorts the list in ascending order
arr.reverse() # reverses the list

n = len(arr)
arr[-1] # last element of the list

# slicing the array
arr[1:3]

arr.clear() # clears all items

# list comprehension for creating a new list based on an existing list
# c# var squares = list.Select(x => x * x).ToList();

squares = [x * x for x in arr if x > 1]

# build dictionary and sets
pairs = [("a", 1), ("b", 2), ("c", 0)]
freq = {k: v for k, v in pairs if v > 0 }
print(freq)
