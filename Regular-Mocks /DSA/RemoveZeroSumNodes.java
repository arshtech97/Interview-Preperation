// PS: https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

 /*
    [1, 2, 3, -3, -2]
    [1  3  6   3   1]

    [1, 2, -3]
    [1, 3, 0]

    [1, 2, 3, -3, -2]
    [1, 3, 6, 3, 1]

    T.C: O(N), S.C: O(N)

 */
class Solution {

    public ListNode removeZeroSumSublists(ListNode head) {
        ListNode front = new ListNode(0, head); // Check this if it fails
        Map<Integer, ListNode> map = new HashMap();
        int prefixSum = 0;
        ListNode curr = front;
        
        // Fill in the prefix map
        while(curr != null){
            prefixSum += curr.val;
            map.put(prefixSum, curr);
            curr = curr.next;
        }
        
        curr = front;
        prefixSum = 0;

        while(curr != null){
            prefixSum += curr.val;
            // map[prefixSum].next ;
            curr.next = map.get(prefixSum).next;
            curr = curr.next;
        }

        return front.next;
    }
}