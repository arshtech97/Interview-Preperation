// PS: https://leetcode.com/problems/find-the-pivot-integer

class Solution {
    public int pivotInteger(int n) {
        int forwardSum = (n * (n + 1))/2;
        int backwardSum = 0;

        for (int i = n; i >= 1; i--){
            backwardSum += i;
            if (backwardSum == forwardSum){
                return i;
            }
            forwardSum -= i;
        }
        return -1;
    }
}