class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        set<int> st;
        // [111, 011, 001] -> [7, 3, 1]
        for(string num : nums){
            st.insert(stoi(num, 0, 2)); // [7, 3, 1]
        }

        int n = nums.size(); // [0, 1, 10, 11] -> [0, 1, 2, 3]
        for(int i = 0; i <= n; i++){
            if(st.count(i) == 0){
                string ans = bitset<16>(i).to_string();
                // cout << ans << endl;
                return ans.substr(16 - n); // 13 -> end
            }
        }

        return "";
    }
};