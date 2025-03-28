class Solution {
public:
    vector<int> maxPoints(vector<vector<int>>& g, vector<int>& q) {
        int k = q.size(), n = g.size(), m = g[0].size();
        vector<pair<int, int>> tmp;
        for (int i = 0; i < k; i++) {
            tmp.push_back({q[i], i});
        }
        sort(tmp.begin(), tmp.end());
        vector<int> ans(k);
        priority_queue<pair<int, pair<int, int>>,
                       vector<pair<int, pair<int, int>>>,
                       greater<pair<int, pair<int, int>>>>
            pq;
        pq.push({g[0][0], {0, 0}});
        vector<vector<bool>> vis(n, vector<bool>(m));
        vector<vector<int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int sum = 0;
        vis[0][0] = true;
        for (auto [query, index] : tmp) {

            while (!pq.empty() && pq.top().first < query) {
                int row = pq.top().second.first, col = pq.top().second.second;
                pq.pop();
                sum++;
                for (auto dir : dirs) {
                    int newRow = row + dir[0];
                    int newCol = col + dir[1];
                    if (newRow >= 0 && newRow < n && newCol >= 0 &&
                        newCol < m && !vis[newRow][newCol]) {
                        vis[newRow][newCol] = true;
                        pq.push({g[newRow][newCol], {newRow, newCol}});
                    }
                }
            }
            ans[index] = sum;
        }

        return ans;
    }
};