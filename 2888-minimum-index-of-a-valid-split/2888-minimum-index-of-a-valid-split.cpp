class Solution {
public:
    int minimumIndex(vector<int>& nums) {
        // we can not sort nums
        // we check the first half till it be valid
        // then we check the second 
        // if both valid return first index
        // 0 1 2 3  second = n - index - 1, first = index + 1
        // 1 2 2 2 -> freq * 2 > size
        // mp1 -> {1, 1}
        // mp2 -> {2, 3}
        map<int, int> mpf, mps;
        int n= nums.size();

        for(int i = 0; i < n; i++){
            mps[nums[i]]++;
        }

        for(int i = 0; i < n; i++){
            mpf[nums[i]]++;
            mps[nums[i]]--;
            if(mpf[nums[i]] * 2 > i + 1 && mps[nums[i]] * 2 > n - i - 1){
                return i;
            }
        }
        return -1;
    }
};