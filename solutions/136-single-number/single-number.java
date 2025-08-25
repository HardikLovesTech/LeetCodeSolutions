class Solution {
    public int singleNumber(int[] nums) {
        if(nums.length == 1){
            return nums[0];
        }
        else{
            Map<Integer , Integer> NumberCounts = new HashMap<>();

            for(int numebr : nums){
                if(NumberCounts.containsKey(numebr)){
                    int currentCount = NumberCounts.get(numebr);
                    NumberCounts.put(numebr , currentCount + 1);
                }else{
                    NumberCounts.put(numebr , 1);
                }
            }

            for (Map.Entry<Integer, Integer> entry : NumberCounts.entrySet()) {
                if (entry.getValue() != 2) {
                    return entry.getKey();
                }
            }


        }
    return -1;

    }
}