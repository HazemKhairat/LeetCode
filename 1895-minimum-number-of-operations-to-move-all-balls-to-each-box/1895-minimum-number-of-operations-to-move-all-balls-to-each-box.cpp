class Solution {
public:
    vector<int> minOperations(string boxes) {
        vector<int> res(boxes.size());
        for (int i = 0; i < boxes.size(); i++) {
            int ans = 0;
            for (int j = 0; j < boxes.size(); j++) {
                if (boxes[j] == '1') {
                    ans += abs(j - i);
                }
            }
            res[i] = ans;
        }
        return res;
    }
};