class Solution {
public:
    int mostProfitablePath(vector<vector<int>>& edges, int bob,
                           vector<int>& amount) {
        int n = amount.size(), maxIncome = INT_MIN;
        graph.resize(n);
        visited.assign(n, false);
        queue<vector<int>> nodeQueue;
        nodeQueue.push({0, 0, 0});
        for (auto edge : edges) {
            int u = edge[0], v = edge[1];
            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        findBobPath(bob, 0);

        visited.assign(n, false);

        while (!nodeQueue.empty()) {
            int source = nodeQueue.front()[0], time = nodeQueue.front()[1],
                income = nodeQueue.front()[2];

            if (!BobPath.count(source) || BobPath[source] > time) {
                income += amount[source];
            } else if (BobPath[source] == time) {
                income += amount[source] / 2;
            }

            if (graph[source].size() == 1 && source != 0) {
                maxIncome = max(maxIncome, income);
            }

            for (int adj : graph[source]) {
                if (!visited[adj]) {
                    nodeQueue.push({adj, time + 1, income});
                }
            }

            visited[source] = true;
            nodeQueue.pop();
        }

        return maxIncome;
    }

private:
    vector<vector<int>> graph;
    vector<int> visited;
    map<int, int> BobPath;

    bool findBobPath(int sourceNode, int time) {
        BobPath[sourceNode] = time;
        visited[sourceNode] = true;

        if (sourceNode == 0) {
            return true;
        }
        for (auto nighbour : graph[sourceNode]) {
            if (!visited[nighbour]) {
                if (findBobPath(nighbour, time + 1)) {
                    return true;
                }
            }
        }

        BobPath.erase(sourceNode);
        return false;
    }
};