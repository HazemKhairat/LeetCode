class Solution {
public:
    vector<int>memo;
    int findLongestChain(vector<vector<int>>& pairs) {
        sort(pairs.begin(), pairs.end(),
             [](const vector<int>& a, const vector<int>& b) {
                 return a[1] < b[1];
             });
        int n = pairs.size();
        memo = vector<int>(n, 0);
        return solve(pairs, 0, INT_MIN);
    }

    int solve(vector<vector<int>>& pairs, int index, int prev) {
        if (index == pairs.size()) {
            return 0;
        }
        if(memo[index]){
            return memo[index];
        }
        int take = 0, skip = 0;
        if (prev < pairs[index][0]) {
            take = 1 + solve(pairs, index + 1, pairs[index][1]);
        }
        skip = solve(pairs, index + 1, prev);

        return memo[index] = max(take, skip);
    }
};