class Solution {
public:
    // map<pair<int, int>, bool> dp;
    bool stoneGame(vector<int>& piles) {
        return true;
    }

    // bool dfs(vector<int>& piles, int i, int j, int alice, int bob, int turn){
    //     if(j < i){
    //         return (alice > bob);
    //     }
    //     if(dp.count({i, j}) != 0){
    //         return dp[{i, j}];
    //     }
    //     if(turn % 2 == 0){
    //         return dp[{i, j}] = dfs(piles, i + 1, j, alice + piles[i], bob, turn + 1) ||
    //         dfs(piles, i, j - 1, alice + piles[j], bob, turn + 1);
    //     }
    //     else{
    //         return dp[{i, j}] = dfs(piles, i + 1, j, alice, bob + piles[i], turn + 1) ||
    //         dfs(piles, i, j - 1, alice, bob + piles[j], turn + 1);
    //     }
    // }
};