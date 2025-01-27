class Solution {
public:
    vector<bool> checkIfPrerequisite(int numCourses, vector<vector<int>>& prerequisites, vector<vector<int>>& queries) {
        map<int, vector<int>> adj;
        for(auto edge : prerequisites){
            int u = edge[0], v = edge[1];
            adj[u].push_back(v);
        }

        vector<bool> ans;

        for(auto q : queries){
            vector<bool> visited(numCourses, false);
            ans.push_back(isPrerequisite(adj, visited, q[0], q[1]));
        }

        return ans;
    }


    bool isPrerequisite(map<int, vector<int>> &adj, vector<bool> &visited, int src, int dest){
        visited[src] = 1;
        if(src == dest){
            return true;
        }

        int ans = false;

        for(auto edge : adj[src]){
            if(!visited[edge]){
                ans = ans || isPrerequisite(adj, visited, edge, dest);
            }
        }

        return ans;
    }
};