class Solution {
public:
    int ladderLength(string start, string end, vector<string>& wordList) {
        queue<string> q;
        q.push(start);
        unordered_set<string> vis;
        vis.insert(start);
        int count = 1;

        while(!q.empty()){
            int n = q.size();
            for(int i = 0; i < n; i++){
                string curr = q.front();
                if(curr == end) return count;
                q.pop();
                for(auto word : wordList){
                    if(vis.count(word)) continue;
                    int cnt = 0;
                    for(int i = 0; i < word.size(); i++){
                        if(word[i] != curr[i]){
                            cnt++;
                        }
                    }
                    if(cnt == 1){
                        q.push(word);
                        vis.insert(word);
                    }
                }
            }
            count++;
        }
        
        return 0;

    }
};