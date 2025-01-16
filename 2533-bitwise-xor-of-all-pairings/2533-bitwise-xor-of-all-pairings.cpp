class Solution {
public:
    int xorAllNums(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size(), m = nums2.size();
        map<long long, long long> freq;

        for(int i = 0; i < n; i++){
            freq[nums1[i]] += m;
        }
        for(int i = 0; i < m; i++){
            freq[nums2[i]] += n;
        }

        vector<long long> nums3;
        for(auto item : freq){
            if(item.second % 2 == 1){
                nums3.push_back(item.first);
            }
        }

        int res = 0;
        for(auto item : nums3){
            res ^= item;
        }

        return res;


    }
};