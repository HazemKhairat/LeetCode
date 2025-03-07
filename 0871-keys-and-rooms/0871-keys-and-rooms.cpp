class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        vector<bool> visited(rooms.size(), false);
        dfs(rooms, 0, visited);

        for(int i = 0; i < visited.size(); i++){
            if(!visited[i]){
                return false;
            }
        }

        return true;
    }

    void dfs(vector<vector<int>>& rooms, int node, vector<bool>& visited){
        visited[node] = true;
        for(auto nighbour : rooms[node]){
            if(!visited[nighbour]){
                dfs(rooms, nighbour, visited);
            }
        }
    }
};