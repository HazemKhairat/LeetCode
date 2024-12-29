class Solution {
public:
    int numWays(vector<string>& words, string target) {
        vector<vector<int>> dp(words[0].size(), vector<int>(target.size(), -1));
        vector<vector<int>> chFreq(words[0].size(), vector<int>(26));

        for(int i = 0; i < words.size(); i++){
            for(int j = 0; j < words[0].size(); j++){
                int ch = words[i][j] - 'a';
                chFreq[j][ch]++;
            }
        }

        return getWords(words, target, 0, 0, dp, chFreq);

    }

    long getWords(vector<string>& words, string& target, int wordIndex, int targetIndex, 
    vector<vector<int>>& dp, vector<vector<int>>& chFreq){
        if(targetIndex == target.size()) return 1;
        if(wordIndex == words[0].size() || words[0].size() - wordIndex < target.size() - targetIndex){
            return 0;
        }

        if(dp[wordIndex][targetIndex] != -1){
            return dp[wordIndex][targetIndex];
        }
        long countWays = 0;
        int curPos = target[targetIndex] - 'a';

        countWays += getWords(words, target, wordIndex + 1, targetIndex, dp, chFreq);
        countWays += chFreq[wordIndex][curPos] * getWords(words, target, wordIndex + 1, targetIndex + 1
        , dp, chFreq);

        return dp[wordIndex][targetIndex] = countWays % 1000000007;

    }
};