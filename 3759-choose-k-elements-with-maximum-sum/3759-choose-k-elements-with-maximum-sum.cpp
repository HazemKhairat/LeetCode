class Solution {
public:
    vector<long long> findMaxSum(vector<int>& nums1, vector<int>& nums2, int k) {
        int n = nums1.size();
        vector<long long> res(n);
        vector<pair<int, int>> num_idx;
        for(int i = 0; i < n; i++){
            num_idx.push_back({nums1[i], i});
        }
        sort(num_idx.begin(), num_idx.end());

        priority_queue<int, vector<int>, greater<>> pq;
        map<int, long long> mp;
        long long sum = 0;

        int j = 0;
        for(int i = 0; i < n; i++){
            int curr = num_idx[i].second;
            while(j < i){
                int prev = num_idx[j].second;
                
                if(num_idx[j].first == num_idx[i].first) break;

                pq.push(nums2[prev]);
                sum += nums2[prev];
                if(pq.size() > k){
                    sum -= pq.top();
                    pq.pop();
                }
                j++;
            }

            mp[curr] = sum;
        }

        for(int i = 0; i < n; i++){
            res[i] = mp[i];
        }

        return res;
    }
};