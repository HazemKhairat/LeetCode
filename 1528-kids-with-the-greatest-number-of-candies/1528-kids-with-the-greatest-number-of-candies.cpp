class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        priority_queue<int> pq;
        for (auto candy : candies) {
            pq.push(candy);
        }

        vector<bool> res;
        for (int i = 0; i < candies.size(); i++) {
            int curr = candies[i] + extraCandies;
            res.push_back(pq.top() <= curr);
        }

        return res;
    }
};