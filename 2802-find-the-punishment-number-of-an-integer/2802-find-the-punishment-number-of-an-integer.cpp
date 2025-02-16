class Solution {
public:
    int punishmentNumber(int n) {
        int res = 0;
        for (int i = 1; i <= n; i++) {
            if (isPartitioned(0, 0, i, to_string(i * i))) {
                res += (i * i);
            }
        }
        return res;
    }

    bool isPartitioned(int index, int currSum, int target, string str) {
        if (index == str.size()) {
            return currSum == target;
        }

        for (int j = index; j < str.size(); j++) {
            string subStr = str.substr(index, j - index + 1);
            int num = stoi(subStr);
            if (isPartitioned(j + 1, currSum + num, target, str)) {
                return true;
            }
        }

        return false;
    }
};