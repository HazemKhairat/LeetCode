class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        map<int, int> mp;
        for (int item : arr) {
            mp[item]++;
        }

        set<int> st;
        for (auto m : mp) {
            if (st.count(m.second)) {
                return false;
            }
            st.insert(m.second);
        }

        return true;
    }
};