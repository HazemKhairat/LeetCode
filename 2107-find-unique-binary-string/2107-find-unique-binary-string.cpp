class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        set<string> st(nums.begin(), nums.end());
        return backtrack(st, "", nums.size());
    }
    string backtrack(set<string>& st, string str, int n) {
        if (str.size() == n) {
            if (st.count(str) == 0) {
                return str;
            }
            return "";
        }
        string addZero = backtrack(st, str + '0', n);
        if (addZero.size() > 0) {
            return addZero;
        }
        string addOne = backtrack(st, str + '1', n);
        return addOne;
    }
};