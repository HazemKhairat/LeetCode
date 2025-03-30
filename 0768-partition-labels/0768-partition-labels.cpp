class Solution {
public:
    vector<int> partitionLabels(string s) {
        /*
            - use hash map to store freq
            - nested loop to check every char freq == 0
        */

        unordered_map<char, int> freq;
        for (char ch : s) {
            freq[ch]++;
        }

        vector<int> res;
        int l = 0, r = 0;
        while (r < s.size()) {
            freq[s[r]]--;
            bool valid = true;
            for (int i = l; i <= r; i++) {
                if (freq[s[i]] > 0) {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                res.push_back(r - l + 1);
                l = r + 1;
            }
            r++;
        }

        return res;
    }
};