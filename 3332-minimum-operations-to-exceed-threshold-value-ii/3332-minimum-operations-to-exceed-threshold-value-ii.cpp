class Solution {
public:
    int minOperations(vector<int>& nums, int k) {

        priority_queue<long, vector<long>, greater<>> pq;
        for (long long num : nums) {
            pq.push(num);
        }

        int minOperations = 0;
        while (pq.top() < k) {
            long x = pq.top();
            pq.pop();
            long y = pq.top();
            pq.pop();
            long res = (min(x, y) * 2) + max(x, y);
            pq.push(res);
            minOperations++;
        }

        return minOperations;
    }
};