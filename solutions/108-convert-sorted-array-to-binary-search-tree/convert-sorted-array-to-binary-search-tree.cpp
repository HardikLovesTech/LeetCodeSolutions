
class Solution {
public:
    TreeNode* binarySearch(int left, int right, vector<int>& nums)
    {
        if(left > right) return nullptr;
        int mid = (left + right)/2;
        TreeNode* newnode = new TreeNode(nums[mid]);
        newnode -> left = binarySearch(left, mid - 1, nums);
        newnode -> right = binarySearch(mid + 1, right, nums);

        return newnode;
    }

    TreeNode* sortedArrayToBST(vector<int>& nums) {
        int n = nums.size();
        if(n == 1) return new TreeNode(nums[0]);
        TreeNode* root = binarySearch(0, n - 1, nums);
        return root;
    }
};