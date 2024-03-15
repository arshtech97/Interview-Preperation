// PS: https://leetcode.com/problems/custom-sort-string/

import java.util.Map;
import java.util.HashMap;

class Solution {
    /*
        1. HashMap for string s
        2. Move in order and fill up resultant if same char in s
        3. Fill in rest of chars
    */
    public String customSortString(String order, String s) {
        Map<Character, Integer> map = new HashMap();
        StringBuilder result = new StringBuilder();
        
        for(char c: s.toCharArray()){
            if (map.containsKey(c)){
                map.put(c, map.get(c) + 1);
            }else{
                map.put(c, 1);
            }
        }

        for(char c : order.toCharArray()){
            if (map.containsKey(c)){
                while (map.get(c) != 0){
                    result.append(c);
                    map.put(c, map.get(c) - 1);    
                }
            }
        }

        // Now add all those elements which are not present in order.
        for(char key : map.keySet()){
            while (map.get(key) != 0){
                result.append(key);
                map.put(key, map.get(key) - 1);
            }
        }


        return result.toString();
    
    }
}
