class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {
        int left = *max_element(weights.begin(), weights.end());
        int right = accumulate(weights.begin(), weights.end(), 0);
        // cout << left << endl << right;
        while(left <= right){
            int mid = (left + right) / 2;
            if(isPossible(weights, days, mid)){
                right = mid - 1;
            }
            else{
                left = mid + 1;
            }
        }
        return left;
    }

    bool isPossible(vector<int>& weights, int days, int mid){
        int total = 0, d = 1;
        for(int i =0; i < weights.size(); i++){
            total += weights[i];
            if(total > mid){
                total = weights[i];
                d++;
            }
            if(d > days){
                return false;
            }
        }
        return true;
    }
};