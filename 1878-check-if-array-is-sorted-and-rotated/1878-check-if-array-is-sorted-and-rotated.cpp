class Solution {
public:
    bool check(vector<int>& nums) {
        int n = nums.size();
        int firstIntersection = 0;

        for (int i = 0; i < nums.size(); i++) {
            // cout << firstIntersection << endl;
            if (firstIntersection == 1 && i == n - 1) {
                if (nums[i] > nums[0]) {
                    return false;
                }
            } else if (firstIntersection > 1) {
                return false;
            } else if (i < n - 1 && nums[i] > nums[i + 1]) {
                firstIntersection++;
            }
        }
        
        return true;
    }
};