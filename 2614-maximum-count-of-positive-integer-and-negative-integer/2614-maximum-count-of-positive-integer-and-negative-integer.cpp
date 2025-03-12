class Solution {
public:
    int maximumCount(vector<int>& nums) {
        int neg = lowerBound(nums);
        int pos = upperBound(nums);
        return max(neg, pos);
    }

    int lowerBound(vector<int>& nums){
        int left = 0, right = nums.size() - 1, index = nums.size();
        while(left <= right){
            int mid = (left + right) / 2;
            if(nums[mid] >= 0){
                right = mid - 1;
                index = mid;
            }
            else{
                left = mid + 1;
            }
        }
        return index;
    }

    int upperBound(vector<int>& nums){
        int left = 0, right = nums.size() - 1;
        while(left <= right){
            int mid = (left + right) / 2;
            if(nums[mid] <= 0){
                left = mid + 1;
            }
            else{
                right = mid - 1;
            }
        }

        return nums.size() - left ;
    }
};