class Solution {
public:
    int lenLongestFibSubseq(vector<int>& arr) {
        set<int> st(arr.begin(), arr.end());
        int maxLen = 0;

        for (int start = 0; start < arr.size(); start++) {
            for (int next = start + 1; next < arr.size(); next++) {
                int prev = arr[next];
                int curr = arr[start] + prev;
                int len = 2;
                while (st.count(curr)) {
                    len++;
                    int tmp = curr;
                    curr += prev;
                    prev = tmp;
                    maxLen = max(maxLen, len);
                }
            }
        }

        return maxLen;
    }
};