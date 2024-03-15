# PS: https://leetcode.com/problems/custom-sort-string
class Solution:
    """
    
        T.C: O(N), S.C: (N)
        
        1. Map out all the chars and it's frequency from String s and store it in a map
        2. Travserse Order string and check if that character is present in String S if yes add that to resultant string
        3. Now add rest of the characters from String s which are not present in String order
    
    """
    def customSortString(self, order: str, s: str) -> str:
        mapS = {}
        
        for char in s:
            mapS[char] = mapS.get(char, 0) + 1

        # make sure the order remains the same
        result = []

        for key in order:
            if key in mapS:
                while mapS[key]:
                    result.append(key)
                    mapS[key] -= 1
        
        for k, v in mapS.items():
            while mapS[k]:
                result.append(k)
                mapS[k] -= 1


        return ''.join(result)
         
