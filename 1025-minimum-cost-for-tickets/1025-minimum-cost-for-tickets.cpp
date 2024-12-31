class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        int maxDay = days.back();
        vector<int> allDays(maxDay + 1);

        int idx = 0;
        for (int i = 1; i <= maxDay; i++) {
            if (i < days[idx]) {
                allDays[i] = allDays[i - 1];
            } 
            else {
                idx++;
                allDays[i] = min({
                    allDays[i - 1] + costs[0],
                    allDays[max(0, i - 7)] + costs[1],
                    allDays[max(0, i - 30)] + costs[2],
                });
            }
        }

        return allDays[maxDay];
    }
};