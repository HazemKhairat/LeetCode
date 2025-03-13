class Solution {
public:
    int minZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size(), sum = 0, k = 0;
        vector<int> diff(n + 1);

        for(int i = 0; i < n; i++){
            // i = 0, 1, 2
            // nums[i] = 2
            // cout << "k : "  << k << endl;
            while(sum + diff[i] < nums[i]){ // 0 + 2 < 2
                k++; // 1, 2

                if(k > queries.size()){
                    return -1;
                }

                // l = 0, r = 2, val = 1
                int left = queries[k - 1][0], right = queries[k - 1][1], val = queries[k - 1][2];

                if(right >= i){    // 2 >= 0    
                                        // 0 1 2 3
                    diff[max(left, i)] += val;  // 2     -2
                    diff[right + 1] -= val;
                }
            }   
            sum += diff[i]; // 0 + 2 = 2 , 2 + 0 = 2, 2 + 0 = 2;
            // cout << "sum : " << sum << endl;
        }
        return k;
    }
};