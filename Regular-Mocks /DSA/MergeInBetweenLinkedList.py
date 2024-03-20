# PS: https://leetcode.com/problems/merge-in-between-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # T.C: O(N), S.C: O(1)
    # Don't need to worry about the edge case as it will not happen as per constraints.
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        leftNode = list1 # Node just before the 'a' node
        rightNode = list1 # Node just after the 'b' node

        # Place the leftNode
        for i in range(a - 1):
            leftNode = leftNode.next    
        
        # Place the rightNode
        for i in range(b + 1):
            rightNode = rightNode.next 

        # Move to the end of list2
        curr = list2
        
        while curr.next:
            curr = curr.next
        
        lastNode = curr # Last Node of list2

        leftNode.next = list2
        lastNode.next = rightNode

        return list1