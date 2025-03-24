class Solution {
public:
    int countDays(int days, vector<vector<int>>& meetings) {
        map<int, int> mp;
        int sum = 0, freeDays = 0, prevDay = days;

        for (int i = 0; i < meetings.size(); i++) {
            prevDay = min(prevDay, meetings[i][0]);
            mp[meetings[i][0]]++;
            mp[meetings[i][1] + 1]--;
        }

        freeDays += (prevDay - 1);
        for (auto m : mp) {
            int curr = m.first;
            if (sum == 0) {
                freeDays += curr - prevDay;
            }
            sum += m.second;
            prevDay = curr;
        }

        freeDays += days - prevDay + 1;
        return freeDays;
    }
};