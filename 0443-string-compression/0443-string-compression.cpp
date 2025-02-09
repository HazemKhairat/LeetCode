class Solution {
public:
    int compress(vector<char>& chars) {
        if (chars.size() == 1)
            return chars.size();
        string compChars = "";
        int cnt = 1;
        for (int i = 1; i < chars.size(); i++) {
            if (chars[i] == chars[i - 1] && i != chars.size() - 1) {
                cnt++;
            } else {
                if (i == chars.size() - 1 && chars[i] == chars[i - 1]) {
                    cnt++;
                }
                char ch1 = chars[i - 1];
                if (cnt > 1) {
                    string tmp = "";
                    while (cnt) {
                        char ch2 = (cnt % 10) + '0';
                        tmp += ch2;
                        cnt /= 10;
                    }
                    reverse(tmp.begin(), tmp.end());
                    compChars += ch1;
                    compChars += tmp;
                } else {
                    compChars += ch1;
                }
                cnt = 1;
            }
        }
        if(chars[chars.size() - 1] != chars[chars.size() - 2]){
            compChars.push_back(chars[chars.size() - 1]);
        }
        for (int i = 0; i < compChars.size(); i++) {
            chars[i] = compChars[i];
        }

        return compChars.size();
    }
};