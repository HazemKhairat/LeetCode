class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        int curr = values[0];
        int res = 0;
        for(int i = 1; i < values.size(); i++){
            res = max(res, curr + values[i] - i);
            curr = max(curr, values[i] + i);   
        }
        return res;
    }
};