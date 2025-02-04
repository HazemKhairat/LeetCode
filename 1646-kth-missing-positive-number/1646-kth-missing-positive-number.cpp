class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        set<int> st(arr.begin(), arr.end());

        for(int i = 1; i <= 100000; i++){
            if(st.count(i)) continue;
            k--;
            if(k == 0) return i;
        }

        return 0;
    }
};