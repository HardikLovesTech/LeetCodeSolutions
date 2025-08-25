class Solution {
    public int majorityElement(int[] nums) {
        int n = nums.length;
        int half = n/2;
        Map<Integer , Integer> Count= new HashMap<>();
        for(int num : nums){
            Count.put(num , Count.getOrDefault(num , 0)+1);
        }
        for(Map.Entry<Integer , Integer> entry : Count.entrySet()){
            if(entry.getValue() > half){
                return entry.getKey();
            }
        }
        return -1;
    }
}