# PS: https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/?envType=daily-question&envId=2024-03-12

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # 
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0, head)
        start = front 
        prefixSumMap = {}
        prefixSum = 0
        # Calculate teh prefix sum and store them into map
        while start:
            prefixSum += start.val
            prefixSumMap[prefixSum] = start
            start = start.next

        start = front
        prefixSum = 0

        while start:
            prefixSum += start.val
            start.next = prefixSumMap[prefixSum].next
            start = start.next
        
        return front.next

    
    
    
    # Do a simple bruteforce
    # T.C: O(N^2), S.C: O(1)
    def removeZeroSumSublistsBruteForce(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0, head) # dummy-node
        start = front

        while start:
            prefixSum = 0
            end = start.next
            
            # Fix the start and then move end to the end of the list.
            while end:
                prefixSum += end.val
                if prefixSum == 0:
                    start.next = end.next
                end = end.next
            start = start.next
        
        return front.next


        
        