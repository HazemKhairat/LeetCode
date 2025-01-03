class Solution {
public:
    int waysToSplitArray(vector<int>& nums) {
        vector<long long> prefx(nums.begin(), nums.end());
        for (int i = 1; i < prefx.size(); i++) {
            prefx[i] += prefx[i - 1];
        }

        int ans = 0;
        for (int i = 0; i < prefx.size() - 1; i++) {
            long long curr = prefx.back() - prefx[i];
            cout << curr << " " << prefx[i] << endl;
            if (prefx[i] >= curr) {
                ans++;
            }
        }
        return ans;
    }
};