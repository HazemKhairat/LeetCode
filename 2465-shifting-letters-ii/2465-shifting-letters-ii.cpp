class Solution {
public:
    string shiftingLetters(string s, vector<vector<int>>& shifts) {
        int n = s.size();
        vector<int> partialSum(n + 1);
        vector<int> chars;
        for (auto ch : s)
            chars.push_back(ch - 'a');
        for (auto shift : shifts) {
            int start = shift[0], end = shift[1], dir = shift[2];
            if (dir == 1) {
                partialSum[start]++;
                partialSum[end + 1]--;
            } else if (dir == 0) {
                partialSum[start]--;
                partialSum[end + 1] += 1;
            }
        }

        for (int i = 1; i <= n; i++) {
            partialSum[i] += partialSum[i - 1];
            chars[i - 1] += partialSum[i - 1];
        }

        for (int i = 0; i < n; i++) {
            chars[i] = (chars[i] % 26 + 26) % 26;
            cout << chars[i] << " ";
        }

        for (int i = 0; i < s.size(); i++) {
            s[i] = chars[i] + 'a';
        }

        return s;
    }
};