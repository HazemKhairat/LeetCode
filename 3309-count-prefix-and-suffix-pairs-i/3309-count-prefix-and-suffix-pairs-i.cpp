class Solution {
public:
    int countPrefixSuffixPairs(vector<string>& words) {
        int res = 0;
        int n = words.size();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (isPrefixAndSuffix(words[i], words[j])) {
                    res++;
                }
            }
        }
        return res;
    }

    bool isPrefixAndSuffix(string str1, string str2) {
        int n = str2.size() - 1;
        int i = 0, j = str1.size() - 1;
        while (i < str1.size()) {
            if (str1[i] != str2[i] || str1[j] != str2[n - i]) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
};