class Solution {
public:
    int sumIndicesWithKSetBits(vector<int>& nums, int k) {
        int res = 0;
        for(int i= 0; i < nums.size(); i++){
            if(countBits(i) == k){
                res += nums[i];
            }
        }
        return res;
    }

    int countBits(int num){
        int count = 0;
        while(num){
            count += (num & 1);
            num >>= 1;
        }
        return count;
    }
};