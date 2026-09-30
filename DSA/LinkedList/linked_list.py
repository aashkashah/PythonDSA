from DSA.LinkedList.linked_list_base import ListNode

class Solution:
    
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode(0)
        node = dummy
        
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
            
            if list1 is not None:
                node.next = list1
            elif list2 is not None:
                node.next = list2
            
        return dummy.next
    
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
        
    def search(self, nums, target):
        
        if not nums:
            return -1
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid - 1
                else:
                    right = mid - 1
        
        return -1