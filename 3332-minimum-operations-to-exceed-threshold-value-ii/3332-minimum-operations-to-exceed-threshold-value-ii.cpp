class Solution {
public:
    int minOperations(vector<int>& nums, int k) {

        priority_queue<long long, vector<long long>, greater<>> pq;
        for (long long num : nums) {
            pq.push(num);
        }

        long long minOperations = 0;
        while (pq.size() > 1) {
            if (pq.top() >= k) {
                break;
            }
            long long x = pq.top();
            pq.pop();
            long long y = pq.top();
            pq.pop();
            long long res = (min(x, y) * 2) + max(x, y);
            pq.push(res);
            minOperations++;
        }

        return minOperations;
    }
};