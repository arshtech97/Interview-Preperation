// PS: https://leetcode.com/problems/product-of-array-except-self
class Solution {
    // T.C: O(N), S.C: O(N)
    public int[] productExceptSelf(int[] nums) {
        //suffix arr * prefix arr
        int length = nums.length;
        int[] left = new int[length];
        left[0] = 1;
        
        
        for(int i = 1; i < length; i++){
            left[i] = left[i-1] * nums[i-1];
        }

        int rightMul = 1;
        for(int i = length - 1; i >= 0; i--){
            //System.out.println(nums[i]);
            int temp = nums[i];
            nums[i] = rightMul * left[i];
            rightMul *= temp;
        }

        return nums;
    }
}