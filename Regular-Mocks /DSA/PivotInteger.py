# PS: https://leetcode.com/problems/find-the-pivot-integer/

# T.C: O (N), S.C: O(1)
class Solution:
    # n = 8
    # 1 2 3 4 5 6 7 8
    # 1 3 6 10 15 21 28 36 - left To Right
    #.             21  15  8 - right To left
    # here 21 is matching that means on both arrays that means it's our pivot index
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        forwardSum = (n * (n + 1)) // 2 # L -> R
        backwardSum = 0 # R -> L
        for num in range(n, -1, -1):
            backwardSum += num
            print(backwardSum, forwardSum)
            if backwardSum == forwardSum:
                return num
            forwardSum -= num
        return -1