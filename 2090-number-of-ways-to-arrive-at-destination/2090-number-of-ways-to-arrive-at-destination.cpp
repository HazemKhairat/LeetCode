class Solution {
public:
    int countPaths(int n, vector<vector<int>>& roads) {
        int MOD = 1e9 + 7;
        vector<vector<pair<int, int>>> graph(n);
        for (auto road : roads) {
            int u = road[0], v = road[1], w = road[2];
            graph[u].push_back({v, w});
            graph[v].push_back({u, w});
        }

        
        vector<long long> shortestTime(n + 10, LLONG_MAX);
        vector<int> pathCount(n, 0);
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> pq;
        shortestTime[0] = 0;
        pathCount[0] = 1;

        pq.push({0, 0});
        while(!pq.empty()){
            long long time = pq.top().first;
            int node = pq.top().second;
            pq.pop();
            if(time > shortestTime[node]) continue;

            for(auto neighbor : graph[node]){
                int n = neighbor.first, t = neighbor.second;
                if(time + t < shortestTime[n]){
                    shortestTime[n] = time + t;
                    pathCount[n] = pathCount[node];
                    pq.push({shortestTime[n], n});
                }
                else if(time + t == shortestTime[n]){
                    pathCount[n] = (pathCount[n] + pathCount[node]) % MOD; 
                }
            }
        }

        return pathCount[n - 1];  
    }
};