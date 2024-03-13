# https://leetcode.com/problems/apple-redistribution-into-boxes/description/

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        # Take the sum of apples array
        # Sort the capacity decreasingly
        sumOfApple = sum(apple)
        capacity.sort(reverse = True)
        
        result = 0
        for num in capacity:
            result += 1
            if num >= sumOfApple:
                return result
            else:
                sumOfApple -= num
        return result
                
        