class Solution {
    public void moveZeroes(int[] nums) {
        int count = 0, temp, backshots = nums.length-1;
        for (int i = nums.length-1; i>=0; i--){ //Traversing From Behind
            while (nums[backshots] != 0 && nums[nums.length-1] == 0){
                backshots--;
            }
            if (nums[i] == 0){ // This checks if it is 0
                int k = i; // Making a new var to replace inside while
                while (k<backshots){ // Till the last posn
                    temp = nums[k+1];
                    nums[k+1] = nums[k];
                    nums[k] = temp;
                    k++;
                }
            }
        }
    }
}