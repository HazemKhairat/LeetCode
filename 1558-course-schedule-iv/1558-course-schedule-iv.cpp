class Solution {
public:
    vector<bool> checkIfPrerequisite(int numCourses,
                                     vector<vector<int>>& prerequisites,
                                     vector<vector<int>>& queries) {
        int n = prerequisites.size();
        vector<set<int>> map(numCourses);
        for (int i = 0; i < n; i++) {
            int u = prerequisites[i][0], v = prerequisites[i][1];
            map[v].insert(u);
        }

        for (int i = 0; i < numCourses; i++) {
            vector<int> visited(numCourses, false);
            dfs(i, map, i, visited);
        }

        vector<bool> res;
        for (auto query : queries) {
            int course = query[1], prereqest = query[0];
            if (map[course].count(prereqest) > 0) {
                res.push_back(true);
            } else {
                res.push_back(false);
            }
        }

        return res;
    }

    void dfs(int course, vector<set<int>>& map, int& fixedCourse, vector<int>& visited) {
        visited[course] = true;
        if (map[course].empty()) {
            return;
        }

        for (auto prerequest : map[course]) {
            if (!visited[prerequest]) {
                map[fixedCourse].insert(prerequest);
                dfs(prerequest, map, fixedCourse, visited);
            }
        }
    }
};