class Solution {
public:
    vector<int> findThePrefixCommonArray(vector<int>& A, vector<int>& B) {
        int n = A.size();
        set<int> st;
        vector<int> res(n);
        res[0] += (A[0] == B[0]);
        st.insert(A[0]);
        st.insert(B[0]);
        for (int i = 1; i < n; i++) {
            if (A[i] == B[i]) {
                res[i]++;
            } else {
                if (st.find(A[i]) != st.end()) {
                    res[i]++;
                }
                if (st.find(B[i]) != st.end()) {
                    res[i]++;
                }
            }
            res[i] += res[i - 1];
            st.insert(A[i]);
            st.insert(B[i]);
        }

        return res;
    }
};