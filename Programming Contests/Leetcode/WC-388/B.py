# https://leetcode.com/problems/maximize-happiness-of-selected-children/description/

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # Sort the happiness array into decreasing order
        happiness.sort(reverse = True)
        
        negativeBalance = 0
        index = 0
        result = 0
        while k:
            val = happiness[index] - negativeBalance if happiness[index] - negativeBalance >= 0 else 0
            result +=  val
            index += 1
            negativeBalance += 1
            k -= 1
        return result