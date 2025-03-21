class Solution {
public:
    vector<int> findArray(vector<int>& pref) {
        int start = 0, curr = 0;
        vector<int> res(pref.size());
        for (int i = 0; i < pref.size(); i++) {
            int curr = pref[i];      // 5, 2, 0
            res[i] = (start ^ curr); // 0 ^ 5 = 5, 5 ^ 2 = 7, 2 ^ 0 = 2 ...
            start = curr;            // 5, 2
        }
        return res;
    }
};