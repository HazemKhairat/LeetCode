class Solution {
public:
    int countPalindromicSubsequence(string s) {
        set<char> letters(s.begin(), s.end());
        int ans = 0;

        for(auto letter : letters){
            int i = -1;
            int j = 0;
            for(int k = 0; k < s.size(); k++){
                if(s[k] == letter){
                    if(i == -1){
                        i = k;
                    }

                    j = k;
                }
            }

            set<char> between;
            for(int k = i + 1; k < j; k++){
                between.insert(s[k]);
            }
            ans += between.size();
        }

        return ans;

    }
};