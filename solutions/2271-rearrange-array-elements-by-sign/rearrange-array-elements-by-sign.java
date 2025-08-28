class Solution {
    public int[] rearrangeArray(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];

        List<Integer> pos = new ArrayList<>();
        List<Integer> neg = new ArrayList<>();

        for (int num : nums) {
            if (num > 0) pos.add(num);
            else neg.add(num);
        }

        int i = 0, p = 0, q = 0;
        while (i < n) {
            if (i % 2 == 0) {
                result[i++] = pos.get(p++);
            } else {
                result[i++] = neg.get(q++);
            }
        }

        return result;

    }
}