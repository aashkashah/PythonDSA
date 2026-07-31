
"""Heap data structure implementation in Python.
C# comparision:
var heap = new PriorityQueue<int, int>();
pq.Enqueue(1, 1);
pq.Dequeue(); // returns 1
"""

import heapq

heap = []
heapq.heappush(heap, 1) # adds an element to the heap
heapq.heappush(heap, 3)
smallest =  heapq.heappop(heap) # removes smallest element

print(smallest) 

tuple_heap = []
heapq.heappush(tuple_heap, (-2, "a")) # heap can store tuples, it will compare the first element of the tuple for ordering
heapq.heappush(tuple_heap, (-1, "b"))
heapq.heappush(tuple_heap, (-2, "b"))

print(heapq.heappop(tuple_heap)) # Output: (-2, 'a') because it is the smallest element in the heap 
# max heap is implemented by negating the values


points = [(1, 2), (3, 4), (5, 6)]
max_heap = []
for x, y in points:
    dist = x*x + y*y
    heapq.heappush(max_heap, (-dist, x, y))
    