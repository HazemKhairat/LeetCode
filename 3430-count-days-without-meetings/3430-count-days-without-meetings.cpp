class Solution {
public:
    int countDays(int days, vector<vector<int>>& meetings) {
        sort(meetings.begin(), meetings.end());
        
        int free = 0, maxEnd = 0;
        for(auto meeting : meetings){
            int start = meeting[0], end = meeting[1];
            if(start > maxEnd){
                free += (start - maxEnd) - 1;
            }
            maxEnd = max(maxEnd, end);
        }
        free += (days - maxEnd);
        return free;
    }
};