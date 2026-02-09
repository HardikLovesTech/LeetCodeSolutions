class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        vector<int> DN;
        int i = 1;

        for (int num : nums) {
            if (num == i) {
                i++;
            } else if (num > i) {
                while (i < num) {
                    DN.push_back(i);
                    i++;
                }
                i++;
            }
        }

        while (i <= nums.size()) {
            DN.push_back(i);
            i++;
        }

        return DN;
    }
};
