class Solution {
public:
    bool doesValidArrayExist(vector<int>& derived) {
        int res = 0;
        for(int item : derived){
            res ^= item;
        }
        return res == 0;
    }
};