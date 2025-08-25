class Solution {
    public void sortColors(int[] arr) {
        int max_val = arr[0];
        for(int num : arr) {
            if(num > max_val) {
                max_val = num;
            }
        }

        int[] count = new int[max_val + 1];
        
        for(int num : arr) {
            count[num]++;
        }

        int index = 0;
        for(int i = 0; i <= max_val; i++) {
            while(count[i] > 0) {
                arr[index++] = i;
                count[i]--;
            }
        }
    }
    }
