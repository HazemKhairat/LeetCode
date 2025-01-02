class Solution {
public:
    vector<int> vowelStrings(vector<string>& words,
                             vector<vector<int>>& queries) {
        int n = words.size();
        vector<int> prefx(n + 1);
        int i = 1;
        for (auto word : words) {
            char start = word[0], end = word.back();
            if ((start == 'a' || start == 'e' || start == 'i' || start == 'o' ||
                 start == 'u') &&
                (end == 'a' || end == 'e' || end == 'i' || end == 'o' ||
                 end == 'u')) {
                prefx[i] = prefx[i - 1] + 1;
            } else {
                prefx[i] = prefx[i - 1];
            }
            i++;
        }

        vector<int> ans;
        for (auto query : queries) {
            int left = query[0], right = query[1];
            int res = prefx[right + 1] - prefx[left];
            ans.push_back(res);
        }
        return ans;
    }
};