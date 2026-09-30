class HeapQuestions:
    
    def kthLargest(self, nums, k):
        import heapq
        
        if not nums:
            return 0
        
        heap = []
        
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif num > heap[0]:
                heapq.heappushpop(heap, num)
        
        return heap[0]
        