class Solution {
public:
    map<int, int> memo;
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        return dfs(days, costs, 0);
    }

    int findNextIndex(vector<int>& days, int value) {
        auto it = upper_bound(days.begin(), days.end(), value);
        return distance(days.begin(), it);
    }

    int dfs(vector<int>& days, vector<int>& costs, int idx) {
        int nextIdx = 0;
        if (idx >= days.size()) {
            return 0;
        }
        if (memo.count(idx))
            return memo[idx];
        int One = costs[0] + dfs(days, costs, idx + 1);
        nextIdx = findNextIndex(days, days[idx] + 7 - 1);
        int Seven = costs[1] + dfs(days, costs, nextIdx);
        nextIdx = findNextIndex(days, days[idx] + 30 - 1);
        int Thirty = costs[2] + dfs(days, costs, nextIdx);
        return memo[idx] = min({One, Seven, Thirty});
    }
};