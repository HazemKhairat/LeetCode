class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        /*
                0  1  2 3 4  5  6 7  8  9
            ex: 1,100,1,1,1,100,1,1,100,1

            prev = 1, curr = 100
            index = 9
            tmp = 100 + 5 = 105
            prev = 6
            curr = 105
        */
        int prev = cost[0], curr = cost[1];
        for (int i = 2; i < cost.size(); i++) {
            int tmp = cost[i] + min(prev, curr);
            prev = curr;
            curr = tmp;
        }
        return min(prev, curr);
    }
};