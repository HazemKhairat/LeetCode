class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        const int MOD = 1e9 + 7;
        int n = arr.size();
        vector<int> dpEven(n), dpOdd(n);
        for(auto& num : arr){
            num %= 2;
        }
        
        if(arr[n - 1] == 1){
            dpOdd[n - 1] = 1;
        }
        else{
            dpEven[n - 1] = 1;
        }

        for(int idx = n - 2; idx >= 0; idx--){
            if(arr[idx] == 0){
                dpEven[idx] = (1 + dpEven[idx + 1]) % MOD;
                dpOdd[idx] = dpOdd[idx + 1] ;
            }
            else{
                dpOdd[idx] = (1 + dpEven[idx + 1]) % MOD;
                dpEven[idx] = dpOdd[idx + 1];
            }
        }

        int count = 0;
        for(auto oddCount : dpOdd){
            count += oddCount;
            count %= MOD;
        }

        return count;
    }

};