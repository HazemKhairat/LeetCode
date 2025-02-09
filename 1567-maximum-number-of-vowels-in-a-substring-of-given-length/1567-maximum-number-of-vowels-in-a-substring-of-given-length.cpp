class Solution {
public:
    int maxVowels(string s, int k) {
        string vowels = "aeiou";
        int ans = 0, cnt = 0;
        int i = 0, j = 0;
        while ((i - j) < k) {
            if (vowels.find(s[i]) != string::npos) {
                cnt++;
            }
            i++;
        }
        ans = cnt;
        // cout << i << " " << j << endl;
        while (i < s.size()) {
            // cout << cnt <<endl;
            if (vowels.find(s[i]) != string::npos) {
                cnt++;
            }
            // cout << cnt << endl;
            if (vowels.find(s[j]) != string::npos) {
                cnt--;
            }
            // cout << cnt << " ," << s[i] << " , " << s[j - 1] << endl;
            ans = max(ans, cnt);
            i++, j++;
        }

        return ans;
    }
};