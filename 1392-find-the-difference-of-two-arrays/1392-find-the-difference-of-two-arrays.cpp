class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        set<int> st1, st2;
        for(int num : nums1){
            st1.insert(num);
        }
        for(int num : nums2){
            st2.insert(num);
        }  

        vector<int> v1, v2;
        for(int num : nums2){
            if(!st1.count(num)){
                v1.push_back(num);
                st1.insert(num);
            }
        }
        for(int num : nums1){
            if(!st2.count(num)){
                v2.push_back(num);
                st2.insert(num);
            }
        }

        return {v2,v1};


    }
};