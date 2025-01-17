class Solution {
public:
    bool doesValidArrayExist(vector<int>& derived) {
        int ans = 0;
        
        for(auto item : derived){
            ans ^= item;
        }

        return ans == 0;
    }
};