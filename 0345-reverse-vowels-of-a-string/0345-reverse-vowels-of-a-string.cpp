class Solution {
public:
    string reverseVowels(string s) {
        string reversedVowerls = "";
        for (char ch : s) {
            if (tolower(ch) == 'a' || tolower(ch) == 'e' ||
                tolower(ch) == 'i' || tolower(ch) == 'o' ||
                tolower(ch) == 'u') {
                reversedVowerls.push_back(ch);
            }
        }

        for (int i = 0; i < s.size(); i++) {
            char ch = s[i];
            if (tolower(ch) == 'a' || tolower(ch) == 'e' ||
                tolower(ch) == 'i' || tolower(ch) == 'o' ||
                tolower(ch) == 'u') {
                s[i] = reversedVowerls.back();
                reversedVowerls.pop_back();
            }
        }

        return s;
    }
};