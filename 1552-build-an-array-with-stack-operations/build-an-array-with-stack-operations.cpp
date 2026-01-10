class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        vector<string> result;
        int idx = 0;

        for (int num = 1; num <= n && idx < target.size(); num++) {
            result.push_back("Push");

            if (num == target[idx]) {
                idx++;
            } else {
                result.push_back("Pop");
            }
        }
        return result;
    }
};
