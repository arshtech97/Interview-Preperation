# https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/description/

class Solution:
    """
        1. Build a HashMap contaning all the substrings of all the strings present.
        2. Then one by one visit every substring and subtract all those strings present in the HashMap
        3. Now after removing those substrings generate all the substrings for that string and check in HashMap
        4. If it is present that means there exists a substring in another strings
        5. Now rebuild the Map
    """
    
    
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        
        def destroyAndRebuild(str, map):
            #print(map)
            # Remove all the substrings present inside the map for this string
            for size in range(1, len(str) + 1):
                for start in range(len(str) - size + 1):
                    substring = str[start : start + size]
                    map[substring] -= 1
                    if map[substring] == 0:
                        del map[substring]
            
            result = "" # Resultant String

            # Again Traverse the keys and now check whether they are present in the map
            for size in range(1, len(str) + 1):
                for start in range(len(str) - size + 1):
                    substring = str[start : start + size]
                    if substring not in map:
                        print('Adding substring to result: ', substring)
                        if len(result) == 0 or result > substring:
                            result = substring
                if len(result) > 0:
                    break
            
            buildMap(str, map)
            
            return result
                            

        def buildMap(string, map):
            # Generate all substrings and store them into map
            for size in range(1, len(string)+1):
                for start in range(len(string) - size + 1): # check this if code fails
                    substring = string[start: start + size]
                    map[substring] = map.get(substring, 0) + 1
    
        map = {}
        result = []
        for string in arr:
            buildMap(string, map)
        #print(map)
        for str in arr:
            result.append(destroyAndRebuild(str, map))
        return result




        