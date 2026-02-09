class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n = nums.size();
        vector<int> count (n+1 , 0);
        vector<int> result(2);
        for(int num : nums){
            count[num]++;
        }
        for(int i = 0 ; i <= n ; i++){
            if(count[i] == 2) result[0] = i;
            if(count[i] == 0) result[1] = i;
        }
        return result;
    }
};