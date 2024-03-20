# PS: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons

class Solution:
    # T.C: O(NlogN), S.C: O(1)
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Intersect the overlapping intervals and then reutrn the count 
        # Sort on the basis of start first
        points.sort(key = lambda x: x[0])
        result = []
        for point in points:
            s, e = point[0], point[1]
            if len(result) == 0 or result[-1][1] < s:
                result.append(point)
            else:
                result[-1][0] = max(result[-1][0], s)
                result[-1][1] = min(result[-1][1], e)
        return len(result)
        