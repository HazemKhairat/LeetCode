class Solution {
public:
    int minMutation(string start, string end, vector<string>& bank) {
        if (find(bank.begin(), bank.end(), end) == bank.end()) {
            return -1;
        }

        queue<string> q;
        q.push(start);
        unordered_set<string> vis;
        vis.insert(start);
        int res = 0;

        while (!q.empty()) {
            int n = q.size();
            for (int i = 0; i < n; i++) {
                string curr = q.front();
                if (curr == end) {
                    return res;
                }
                q.pop();
                for (auto gene : bank) {
                    if (vis.count(gene))
                        continue;
                    int cnt = 0;
                    for (int j = 0; j < gene.size(); j++) {
                        if (gene[j] != curr[j]) {
                            cnt++;
                        }
                    }
                    if (cnt == 1) {
                        q.push(gene);
                        vis.insert(gene);
                    }
                }
            }

            res++;
        }

        return -1;
    }
};