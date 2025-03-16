class Solution {
public:
    vector<int> answerQueries(vector<int>& nums, vector<int>& queries) {
        sort(nums.begin(), nums.end());
        for (int i = 1; i < nums.size(); i++) {
            nums[i] += nums[i - 1];
            // cout << nums[i] << " ";
        }

        for (int i = 0; i < queries.size(); i++) {
            queries[i] = search(nums, queries[i]);

        }

        return queries;
    }

    int search(vector<int>& nums, int q){
        int i = 0, j = nums.size() - 1; 
        while(i <= j){
            int mid = (i + j) / 2;
            if(nums[mid] <= q){
                i = mid + 1;
            }
            else if(nums[mid] > q){
                j = mid - 1;
            }
        }

        return i;
    }
};