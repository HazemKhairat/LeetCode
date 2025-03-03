class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        vector<int> values(10001, 0);
        for(auto num : nums){
            values[num] += num;
        }

        int take = 0 , skip = 0;
        for(int i = 0; i < values.size(); i++){
            int takei = skip + values[i];
            int skipi = max(skip, take);
            take = takei;
            skip = skipi;
        }

        return max(take, skip);
    }
};